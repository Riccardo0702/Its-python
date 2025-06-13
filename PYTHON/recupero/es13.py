def is_valid_ipv4(indirizzoip: str) -> bool:

    parts_indirizzoip: list[str] = indirizzoip.split('.')

    if len(parts_indirizzoip) > 4 or len(parts_indirizzoip) < 4:
        return False
    
    for part in parts_indirizzoip:
        
        if part.isdigit() == False:
            return False
        
        elif not 0 <= int(part) <= 255:
            return False
        
        
    return True

is_valid_ipv4("192.168.0.1")
is_valid_ipv4("255.255.255.255")
is_valid_ipv4("256.100.10.1")
is_valid_ipv4("192.168.1")
is_valid_ipv4("192.168.1.a")