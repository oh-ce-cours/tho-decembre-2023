from pathlib import Path
import shutil
import os
import tarfile
import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import filetype  # pip install filetype


def recover_extension_name(fname):
    kind = filetype.guess(fname)
    extension = "unknown"
    if kind is not None:
        extension = kind.extension
    return extension, f".{extension}"


def change_extension(name: Path, extension: str):
    return name.parts[-1].split(".")[0] + extension


def untar(tarfile_name, extract_path):
    if tarfile_name.endswith("tar.gz"):
        tar = tarfile.open(tarfile_name, "r:gz")
        tar.extractall(extract_path)
        tar.close()
    elif tarfile_name.endswith("tar"):
        tar = tarfile.open(tarfile_name, "r:")
        tar.extractall(extract_path)
        tar.close()


def send_email(attached_filename):
    # https://realpython.com/python-send-email/
    subject = "An email with attachment from Python"
    body = "This is an email with attachment sent from Python"
    sender_email = "my@gmail.com"
    receiver_email = "your@gmail.com"

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email  # Recommended for mass emails

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    filename = attached_filename  # In same directory as script

    # Open PDF file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    # Log in to server using secure context and send email
    with smtplib.SMTP("localhost", port=1025) as server:
        # server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)


def main():
    untar("fichiersVrac.tar.gz", "fichiersVrac")
    new_folder = Path("./extensions_recovered")
    to_recovers = list(Path("./fichiersVrac").glob("*"))
    extensions = [recover_extension_name(f) for f in to_recovers]
    for (file_type, extension), to_recover in zip(extensions, to_recovers):
        new_name = change_extension(to_recover, extension)
        print(to_recover, new_name)
        new_path = new_folder / file_type / new_name
        new_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(to_recover, new_path)
    shutil.make_archive("extensions_recovered", format="zip", root_dir=str(new_folder))

    send_email("extensions_recovered.zip")
    shutil.rmtree("fichiersVrac")
    shutil.rmtree(new_folder)
    os.remove("extensions_recovered.zip")


main()
