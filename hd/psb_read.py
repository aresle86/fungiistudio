# Đọc file PSB không cần thư viện: liệt kê lớp, xuất từng lớp ra PNG có nền trong. python3 psb_read.py file.psb thư_mục_ra
import struct,sys,zlib,os
f=open(sys.argv[1],'rb').read(); out=sys.argv[2]; os.makedirs(out,exist_ok=True)
p=0
def rd(fmt):
    global p
    v=struct.unpack_from('>'+fmt,f,p); p+=struct.calcsize('>'+fmt); return v if len(v)>1 else v[0]
sig,ver=rd('4sH'); assert sig==b'8BPS'; big=ver==2; p+=6; ch,H,W,depth,mode=rd('HIIHH'); print('file',W,H,'depth',depth,'mode',mode,'channels',ch)
n=rd('I'); p+=n; n=rd('I'); p+=n
LI=lambda: rd('Q') if big else rd('I')
mi=LI(); mi_end=p+mi; li=LI(); li_end=p+li
cnt=rd('h'); cnt=abs(cnt); layers=[]
LONG={b'LMsk',b'Lr16',b'Lr32',b'Layr',b'Mt16',b'Mt32',b'Mtrn',b'Alph',b'FMsk',b'lnk2',b'FEid',b'FXid',b'PxSD',b'cinf'}
for i in range(cnt):
    t,l,b,r=rd('iiii'); nc=rd('H'); chs=[]
    for c in range(nc):
        cid=rd('h'); ln=LI(); chs.append((cid,ln))
    s=rd('4s'); bk=rd('4s'); op,clip,flags,_=rd('BBBB'); ex=rd('I'); ee=p+ex
    m=rd('I'); p+=m; bl=rd('I'); p+=bl
    nl=f[p]; name=f[p+1:p+1+nl].decode('latin1'); p+=((nl+1+3)//4)*4
    while p<ee:
        sg=rd('4s'); key=rd('4s')
        L=rd('Q') if big and key in LONG else rd('I')
        if key==b'luni':
            k=struct.unpack_from('>I',f,p)[0]; name=f[p+4:p+4+k*2].decode('utf-16-be')
        p+=L
        if sg==b'8BIM' or True: p+= (4-(L%4))%4 if False else 0
        if L%2 and sg in (b'8BIM',b'8B64'): pass
    p=ee
    layers.append(dict(name=name,t=t,l=l,b=b,r=r,chs=chs,op=op,flags=flags,bk=bk))
for i,L in enumerate(layers):
    w=L['r']-L['l']; h=L['b']-L['t']; data={}
    for cid,ln in L['chs']:
        st=p; comp=rd('H'); 
        if cid in (-1,0,1,2) and w>0 and h>0:
            if comp==0: data[cid]=f[p:p+w*h]
            elif comp==1:
                cs=struct.unpack_from('>%d%s'%(h,'I' if big else 'H'),f,p); q=p+h*(4 if big else 2); rows=bytearray()
                for c in cs:
                    e=q+c
                    while q<e:
                        v=f[q]; q+=1
                        if v<128: rows+=f[q:q+v+1]; q+=v+1
                        elif v>128: rows+=bytes([f[q]])*(257-v); q+=1
                data[cid]=bytes(rows)
            else: data[cid]=None
        p=st+ln
    vis=not (L['flags']&2); L['vis']=vis
    print(i,repr(L['name']),'bbox',L['l'],L['t'],L['r'],L['b'],'size',w,h,'vis',vis,'op',L['op'],'blend',L['bk'].decode(),'chs',[c for c,_ in L['chs']])
    if w<=0 or h<=0 or 0 not in data or data.get(0) is None: continue
    R=data[0];G=data.get(1,R);B=data.get(2,R);A=data.get(-1) or b'\xff'*(w*h)
    raw=bytearray()
    for y in range(h):
        raw.append(0); o=y*w; row=bytearray(w*4); row[0::4]=R[o:o+w]; row[1::4]=G[o:o+w]; row[2::4]=B[o:o+w]; row[3::4]=A[o:o+w]; raw+=row
    def ck(t,d): c=struct.pack('>I',len(d))+t+d; return c+struct.pack('>I',zlib.crc32(t+d))
    png=b'\x89PNG\r\n\x1a\n'+ck(b'IHDR',struct.pack('>IIBBBBB',w,h,8,6,0,0,0))+ck(b'IDAT',zlib.compress(bytes(raw),6))+ck(b'IEND',b'')
    open(f'{out}/{i:02d}.png','wb').write(png)
