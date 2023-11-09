# HashALLtheKirbis.py

<p align="center"><img width=500 alt="HashALLtheKirbis.py" src="https://raw.githubusercontent.com/austynguo/HashALLtheKirbis.py/master/Design/hash-omnom.png"></p>

## Overview
`HashALLtheKirbis.py` is a Python script designed to process multiple Kerberos ticket files (`.kirbi`) extracted via Mimikatz. It parses the tickets into a format compatible with password-cracking tools like JohnTheRipper or Hashcat. The script consolidates the extracted tickets into a single output file, prefixed with a timestamp for easy identification.

## Features
- Parses multiple `.kirbi` files from a specified directory.
- Generates a combined text file with a unique timestamp.
- Outputs in a format suitable for use with cracking tools.

## Usage
To use `HashALLtheKirbis.py`, provide the directory containing your `.kirbi` files using the `-d` flag and optionally specify an output filename with the `-o` flag:

```shell
python3 HashALLtheKirbis.py -d /path/to/kirbi/files -o optional_output_filename.txt
```

If no output filename is specified, the script will automatically generate one with the current timestamp.

Running the script with the following command:

```shell
python3 kirbi_ticket_extractor.py -d .
```

will result in an output file named `YYYY-MM-DD-HH.MM_combined.txt` in the current directory, containing all the parsed tickets from `.kirbi` files within that directory.

## Attributions

This script is based on [work](https://github.com/openwall/john/blob/bleeding-jumbo/run/kirbi2john.py) by Tim Medin and Michael Kramer and has been modified for additional functionality by Austyn Guo. It is provided under the Apache License, Version 2.0.

## License

This project is licensed under the Apache License, Version 2.0 - see the [LICENSE](#) file for details.

# Contact
This software does not offer any kind of guarantee. Its use is exclusive for educational environments and / or security audits with the corresponding consent of the client. I am not responsible for its misuse or for any possible damage caused by it.
