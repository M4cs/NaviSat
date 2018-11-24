def displayhelp():
    from terminaltables import SingleTable
    table_data = [
        ['Command', 'Description'],
        ['search', 'Search For Nearby Satellites'],
        ['rpasses', 'See Upcoming Radio Passes'],
        ['vpasses', 'See Upcoming Visual Passes'],
        ['reset', 'Reset your configuration'],
        ['exit', 'Exit NaviSat']
    ]
    table = SingleTable(table_data)
    print(table.table)