import numpy as np
import os
import sqlite3
import pyprind

segy_binary_header_dtype = np.dtype([
    ('binhdr1', '>i4'),
    ('binhdr2', '>i4'),
    ('binhdr3', '>i4'),
    ('binhdr4', '>i2'),
    ('binhdr5', '>i2'),
    ('binhdr6', '>u2'),
    ('binhdr7', '>u2'),
    ('binhdr8', '>u2'),
    ('binhdr9' , '>u2'),
    ('binhdr10' , '>i2'),
    ('binhdr11', '>i2'),
    ('binhdr12', '>i2'),
    ('binhdr13', '>i2'),
    ('binhdr14', '>i2'),
    ('binhdr15', '>i2'),
    ('binhdr16', '>i2'),
    ('binhdr17', '>i2'),
    ('binhdr18', '>i2'),
    ('binhdr19', '>i2'),
    ('binhdr20', '>i2'),
    ('binhdr21', '>i2'),
    ('binhdr22', '>i2'),
    ('binhdr23', '>i2'),
    ('binhdr24', '>i2'),
    ('binhdr25', '>i2'),
    ('binhdr26', '>i2'),
    ('binhdr27', '>i2'),
    ('binhdr28', '>i2'),
    ('binhdr29', '>i2'),
    ('binhdr30', '>i2'),
    ('binhdr31', '>i2'),
    ('binhdr32', '>i2'),
    ('binhdr33', '>i4'),
    ('binhdr34', '>i4'),
    ('binhdr35', '>i4'),
    ('binhdr36', '>i4'),
    ('binhdr37', '>i4'),
    ('binhdr38', '>i4'),
    ('binhdr39', '>i4'),
    ('binhdr40', '>i4'),
    ('binhdr41', '>i4'),
    ('binhdr42', '>i4'),
    ('binhdr43', '>i4'),
    ('binhdr44', '>i4'),
    ('binhdr45', '>i4'),
    ('binhdr46', '>i4'),
    ('binhdr47', '>i4'),
    ('binhdr48', '>i4'),
    ('binhdr49', '>i4'),
    ('binhdr50', '>i4'),
    ('binhdr51', '>i4'),
    ('binhdr52', '>i4'),
    ('binhdr53', '>i4'),
    ('binhdr54', '>i4'),
    ('binhdr55', '>i4'),
    ('binhdr56', '>i4'),
    ('binhdr57', '>i4'),
    ('binhdr58', '>i4'),
    ('binhdr59', '>i4'),
    ('binhdr60', '>i4'),
    ('binhdr61', '>i4'),
    ('binhdr62', '>i4'),
    ('binhdr63', '>i4'),
    ('binhdr64', '>i4'),
    ('binhdr65', '>i4'),
    ('binhdr66', '>i4'),
    ('binhdr67', '>i4'),
    ('binhdr68', '>i4'),
    ('binhdr69', '>i4'),
    ('binhdr70', '>i4'),
    ('binhdr71', '>i4'),
    ('binhdr72', '>i4'),
    ('binhdr73', '>i4'),
    ('binhdr74', '>i4'),
    ('binhdr75', '>i4'),
    ('binhdr76', '>i4'),
    ('binhdr77', '>i4'),
    ('binhdr78', '>i4'),
    ('binhdr79', '>i4'),
    ('binhdr80', '>i4'),
    ('binhdr81', '>i4'),
    ('binhdr82', '>i4'),
    ('binhdr83', '>i4'),
    ('binhdr84', '>i4'),
    ('binhdr85', '>i4'),
    ('binhdr86', '>i4'),
    ('binhdr87', '>i4'),
    ('binhdr88', '>i4'),
    ('binhdr89', '>i4'),
    ('binhdr90', '>i4'),
    ('binhdr91', '>i4'),
    ('binhdr92', '>i4'),
    ('binhdr93', '>i4'),
    ('binhdr94', '>i4'),
    ('binhdr95', '>i4'),
    ('binhdr96', '>i4'),
    ('binhdr97', '>i4'),
    ('binhdr98', '>i4'),
    ('binhdr99', '>i4'),
    ('binhdr100', '>i4'),
    ('binhdr101', '>i4'),
    ('binhdr102', '>i4'),
    ('binhdr103', '>i4'),
    ('binhdr104', '>i4'),
    ('binhdr105', '>i4'),
    ('binhdr106', '>i4'),
    ('binhdr107', '>i4'),
    ('binhdr108', '>i4'),
    ('binhdr109', '>i4'),
    ('binhdr110', '>i4'),
    ('binhdr111', '>i4'),
    ('binhdr112', '>i4'),
    ('binhdr113', '>i4'),
    ('binhdr114', '>i4'),
    ('binhdr115', '>i2'),
])
segy_trace_header_dtype = np.dtype([
    ('th1', '>i4'),
    ('th2', '>i4'),
    ('th3', '>i4'),
    ('th4', '>i4'),
    ('th5', '>i4'),
    ('th6', '>i4'),
    ('th7', '>i4'),
    ('th8', '>i4'),
    ('th9', '>i4'),
    ('th10', '>i4'),
    ('th11', '>i4'),
    ('th12', '>i4'),
    ('th13', '>i4'),
    ('th14', '>i4'),
    ('th15', '>i4'),
    ('th16', '>i4'),
    ('th17', '>i4'),
    ('th18', '>i4'),
    ('th19', '>i4'),
    ('th20', '>i4'),
    ('th21', '>i4'),
    ('th22', '>i4'),
    ('th23', '>i4'),
    ('th24', '>i4'),
    ('th25', '>i4'),
    ('th26', '>i4'),
    ('th27', '>i4'),
    ('th28', '>i4'),
    ('th29', '>i4'),
    ('th30', '>i4'),
    ('th31', '>i4'),
    ('th32', '>i4'),
    ('th33', '>i4'),
    ('th34', '>i4'),
    ('th35', '>i4'),
    ('th36', '>i4'),
    ('th37', '>i4'),
    ('th38', '>i4'),
    ('th39', '>i4'),
    ('th40', '>i4'),
    ('th41', '>i4'),
    ('th42', '>i4'),
    ('th43', '>i4'),
    ('th44', '>i4'),
    ('th45', '>i4'),
    ('th46', '>i4'),
    ('th47', '>i4'),
    ('th48', '>i4'),
    ('th49', '>i4'),
    ('th50', '>i4'),
    ('th51', '>i4'),
    ('th52', '>i4'),
    ('th53', '>i4'),
    ('th54', '>i4'),
    ('th55', '>i4'),
    ('th56', '>i4'),
    ('th57', '>i4'),
    ('th58', '>i4'),
    ('th59', '>i4'),
    ('th60', '>i4'),
])


def read_EBCDIC(_file):
    with open(_file,'rb') as f:
        header = np.fromfile(f, dtype='u2', count=int(3200/2))
        if np.any(np.diff(header)):
            f.seek(0)
            return f.read(3200).decode('EBCDIC-CP-BE').encode('ascii')
        else:
            return None

def read_bheader(_file):
    with open(_file, 'rb') as f:
        f.seek(3200)
        binary = np.frombuffer(f.read(400), dtype=segy_binary_header_dtype)
        try:
            assert 0 < binary ['binhdr10'] < 9
        except AssertionError:
            binary = binary.byteswap()
        return binary

def num_traces(_file, ns):
    with open(_file, 'rb') as f:
        f.seek(0, os.SEEK_END)
        size = f.tell()
        nt = (size - 3600.0) / (240.0 + ns * 4.0)
        assert nt % 1 == 0
    return nt


from struct import Struct
class StructIBM32(object):
    def __init__(self,size):
        self.p24 = float(pow(2,24))
        self.unpack32int = Struct(">%sL" %size).unpack
        self.unpackieee = Struct(">%sf" % size).unpack
    def unpackibm(self,data):
        int32 = self.unpack32int(data)
        return [self.ibm2ieee(i) for i in int32]
    def unpackieee(self,data):
        ieee = self.unpackieee(data)
        return ieee
    def unpackedhdr(self,data):
        int32 = self.unpack32int(data)
        return  int32
    def ibm2ieee(self,int32):
        if int32 == 0:
            return 0.0
        sign = int32 >> 31 & 0x01
        exponent = int32 >> 24 & 0x7f
        mantissa = (int32 & 0x00ffffff) / self.p24
        return (1-2*sign)*mantissa*pow(16, exponent - 64)


filename = './DATA/shot.sgy'
# ebcdic = read_EBCDIC(filename)
# print(ebcdic)
binhead=read_bheader(filename)

f = open(filename,'rb')
f.seek(3600)  # to skip 3600 bytes i.e EBCDIC and BINARY Header
ns = binhead[0][7]

ntraces=int(num_traces(filename,ns))

def create_table(name,b):
    conn = sqlite3.connect(name)
    conn.execute('DROP TABLE IF EXISTS mytable')
    columns= ['value%d' % n for n in range(1,b)]
    columns_declaration=','.join('%s REAL' % c for c in columns)
    conn.execute("CREATE TABLE mytable (%s)" %columns_declaration)
    conn.commit()
def insert_table(name,b,c):
    conn = sqlite3.connect(name)
    d = b -1
    placeholders = ', '.join(['?'] * d)
    conn.execute('''INSERT INTO mytable VALUES ({})'''.format(placeholders), c)
    conn.commit()


n=ns+60  # 60 is no of trace header id
tablename="shotdb.db"
create_table(tablename,n+1)
bar = pyprind.ProgBar(ntraces)
traces=[]
for i in range(ntraces):
    bar.update()
    data = f.read((n) * 4)
    hdr=list(np.array(list((np.frombuffer(data[0:240], dtype=segy_trace_header_dtype))[0]))+0.0)  # trace header as float
    amp= StructIBM32(ns).unpackibm(data[240:(ns * 4) + 240])
    headandtrace=hdr+amp #concatenate
    insert_table(tablename, n+1,headandtrace)