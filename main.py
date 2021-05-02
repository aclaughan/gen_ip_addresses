CLASS_C = "152.101.0."
NUM_LANS = 7
NUM_UP_LINKS = 8

def main():
    header = "||subnet|first host|last host|broadcast|description|\n" \
                "|:-|:-|:-|:-|:-|:-|\n"

    device = 0

    # generate the /30 uplink subnets

    output = "# IP Adressing\n\n## Up-links\n" + header

    for serial in range(NUM_UP_LINKS):
        number = int(device/4) + 1
        output += f"|{number}.."
        for host in range(4):
            ip_address = f"|{CLASS_C}{device}"
            output += f"{ip_address}"
            device += 1
        output += f'|link #{number}|\n'

    # generate the /27 VLAN subnets

    output += "<br>\n## Vlan's\n" + header

    for lan in range(NUM_LANS):
        number = int(device/32)
        output += f"|{number}.."
        ip_address = f"|{CLASS_C}{device}|{CLASS_C}{device+1}|{CLASS_C}{device+30}|{CLASS_C}{device+31}"
        output += f"{ip_address}"
        device += 32
        output += f'|vlan #{2000 + number}|\n'


    with open("address.md", 'w') as out_file:
        out_file.write(output)

if __name__ == '__main__':
    main()

