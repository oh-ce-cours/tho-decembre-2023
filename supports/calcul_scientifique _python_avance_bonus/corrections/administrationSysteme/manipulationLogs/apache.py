import re
import geoip2.database
from collections import Counter
from user_agents import parse as ua_parse  # pip install pyyaml ua-parser user-agents
import zipfile
import io
from dateutil import parser

# presentation
from tqdm import tqdm
from rich.console import Console
from rich.table import Table
from rich.progress import track
from termgraph import termgraph, module

# https://github.com/elastic/examples/tree/master/Common%20Data%20Formats/apache_logs


def parser_log_apache_line(ligne):
    """Permet de parser une ligne de log apache.
    On utilise la méthode classique qui consiste en
    une expression régulière adaptée.
    """
    regex = '([(\d\.)]+) - - \[(.*?)\] "(.*?)" (\d+) (\d+) "(.*?)" "(.*?)"'
    # https://httpd.apache.org/docs/2.4/fr/logs.html
    fields = [
        "client_ip",
        "datetime",
        "ressource",
        "status",
        "weight",
        "referer",
        "user_agent",
    ]
    match = re.match(regex, ligne)
    if match:
        return dict(zip(fields, match.groups()))


def augment_parsed_line_ip(reader, parsed: dict):
    response = reader.country(parsed["client_ip"])
    parsed["ip_infos"] = response
    return parsed


def augment_parsed_line_user_agent(parsed):
    parsed["ua_infos"] = ua_parse(parsed["user_agent"])
    return parsed


def parse_lines(lines):
    res = []
    with geoip2.database.Reader(
        "../../medias/analyseLogs/GeoLite2-Country_20220125/GeoLite2-Country.mmdb"
    ) as reader:
        # for line in tqdm(lines):
        for line in track(lines, description="Parsing lines"):
            parsed = parser_log_apache_line(line)
            if not parsed:
                continue
            parsed = augment_parsed_line_ip(reader, parsed)
            parsed = augment_parsed_line_user_agent(parsed)
            res.append(parsed)
    return res


def analyse(parsed):
    analyse_countries(parsed)
    analyse_status_codes(parsed)
    print(
        f"Volume transféré : {sum(int(p['weight']) for p in parsed) / (1024 * 1024):.2f} Mio"
    )
    analyse_calendar(parsed)


def analyse_calendar(parsed):
    print("Vues selon le jour et le mois ")
    dates = []
    for p in parsed:
        # https://nablux.net/tgp/weblog/2013/10/29/parsing-timestamps-apache-log-files-python/
        date_str = p["datetime"][:11] + " " + p["datetime"][12:]
        date = parser.parse(date_str)
        dates.append(date.date().strftime("%Y-%m-%d"))

    dates_count = dict(Counter(dates))
    termgraph.calendar_heatmap(
        data=[i for i in dates_count.values()],
        labels=list(dates_count.keys()),
        args={
            "color": "red",
            "custom_tick": None,
            "start_dt": dates[0],
        },
    )


def analyse_countries(parsed):
    print("Top 10 des pays avec le plus de vues")
    countries = Counter(
        p["ip_infos"].country.names.get("fr", "not found") for p in parsed
    )
    console = Console()
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Pays", style="dim", width=20, justify="right")
    table.add_column("Nombre de hits")
    for pays, count in countries.most_common(10):
        table.add_row(pays, str(count))
    console.print(table)


def analyse_status_codes(parsed):
    print("Status les plus représentés")
    status = Counter(p["status"] for p in parsed)
    console = Console()
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Status", style="dim", width=20, justify="right")
    table.add_column("Nombre de hits")
    for statu, count in status.most_common(10):
        table.add_row(statu, str(count))
    console.print(table)


def main():
    zip_path = "../../medias/analyseLogs/apache.zip"
    with zipfile.ZipFile(zip_path, "r") as myzip:
        with myzip.open("apache.log") as myfile:
            myfile = io.TextIOWrapper(myfile, encoding="utf8", newline="")
            lines = myfile.readlines()
            parsed = parse_lines(lines)
            analyse(parsed)


if __name__ == "__main__":
    main()
