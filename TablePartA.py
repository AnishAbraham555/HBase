import happybase as hb

conn = hb.Connection()

cf = {
    'personal': dict(),
    'professional': dict(),
    'custom':dict()
}

conn.create_table('powers1', cf)
print('Created table powers1')

conn.close()
