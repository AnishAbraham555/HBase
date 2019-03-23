import happybase as hb

conn = hb.Connection()

cf = {
    'personal': dict(),
    'professional': dict(),
    'custom':dict()
}

conn.create_table('powers', cf)
print('Created table powers')

conn.close()
