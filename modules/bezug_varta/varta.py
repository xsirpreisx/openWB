#!/usr/bin/env python3
from typing import List
import logging
import struct
import codecs

from pymodbus.client.sync import ModbusTcpClient

from helpermodules.cli import run_using_positional_cli_args

log = logging.getLogger("Varta EVU")


def update(ipaddress: str):
    with ModbusTcpClient(ipaddress, port=502) as client:
        # gridleistung
        resp = client.read_holding_registers(1078, 1, unit=1)
        value1 = resp.registers[0]
        all = format(value1, '04x')
        final = int(struct.unpack('>h', codecs.decode(all, 'hex'))[0])*-1
        log.debug("Result: %s", str(final))
        with open('/var/www/html/openWB/ramdisk/wattbezug', 'w') as f:
            f.write(str(final))


def main(argv: List[str]):
    run_using_positional_cli_args(update, argv)
