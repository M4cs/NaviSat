def display():
    print("""
Categories:

 [1] Brightest             [2] ISS
 [3] Weather               [4] NOAA
 [5] GOES                  [6] Earth Resources
 [7] Search & Rescue       [8] Disaster Monitoring
 [9] Tracking/Data Relay   [10] Geostationary
 [11] Intelsat             [12] Gorizont
 [13] Raduga               [14] Molniya
 [15] Iridium              [16] Orbcomm
 [17] Globalstar           [18] Amatuer Radio
 [19] Experimental         [20] GPS Operational
 [21] Glonass Operational  [22] Galileo
 [23] S.B.A.S              [24] Navy Nav. Sat. Sys.
 [25] Russian LEO Nav.     [26] Space and Earth Sci.
 [27] Geodetic             [28] Engineering
 [29] Education            [30] Military
 [31] Radar Calibration    [32] CubeSats
 [33] XM and Sirus         [34] TV
 [35] Beidou Nav. Sys.     [36] Yaogan
 [37] Westford Needles     [38] Parus
 [39] Strela               [40] Gonets
 [41] Tsiklon              [42] Tsikada
 [43] O3B Networks         [44] Tselina
 [45] Celestis             [46] IRNSS
 [47] QZSS                 [48] Flock
 [49] Lemur                [50] GPS Constellation
    
      [!] Choose A Category From Above [!]
    """.center(45, " "))
    catid = input("> ")
    return catid
