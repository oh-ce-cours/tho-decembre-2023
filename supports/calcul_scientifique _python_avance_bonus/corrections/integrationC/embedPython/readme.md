# source 

https://docs.python.org/3/extending/embedding.html

# compilation 

Compilation options are specific to installation (virtualenv)

```
python-config --cflags
-I/home/mfalce/Envs/formation_orsys_pya/include/python3.6m -I/home/mfalce/Envs/formation_orsys_pya/include/python3.6m -Wno-unused-result -Wsign-compare -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -g -flto -fuse-linker-plugin -ffat-lto-objects
```

```
python-config --ldflags
-lpython3.6m -lpthread -ldl -lutil -lm -Xlinker -export-dynamic -Wl,-O1 -Wl,-Bsymbolic-functions
```

# Programs 

There are some issues with paths and pythonpath to find embeded.

## Run script

run a script provided in command line 
```
./run_script multiply multiply 3 87
Will compute 3 times 87
Result of call: 261
```

## Run script script string

run a script provided in command line (formats a string by 0 padding)

```
./run_script_string format_string format 32 10
variable 'format_string'
loading 'format_string' module
Result of call: 0000000032
```