def licenseKeyFormatting(S: str, K: int) -> str:
    pool = ''.join(S.split('-'))
    newLicenceKeyGroups = []
    remainder = len(pool) % K 
    if remainder > 0:
      newLicenceKeyGroups.append(pool[0:remainder])
      pool = pool[remainder:]
    while len(pool) > 0:
        newLicenceKeyGroups.append(pool[0:K])
        pool = pool[K:]
    return '-'.join(newLicenceKeyGroups).upper()
