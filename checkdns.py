def get_iplist(domain=""):
    try:
        A = dns.resolver.query(domain,'A')
    except:
        print("01 dns resolver error: ")
        return
    for i in A.response.answer:
        for j in i.items:
            if j.rdtype == 1:
                iplist.append(j.address)
    return True
def checkip(ip):
    checkurl = ip +":80"
    getcontent=""
    http.client.socket.setdefaulttimeout(5)
    conn=http.client.HTTPConnection(checkurl)
    try:
        conn.request("GET","/",headers={"Host":domain})
        r=conn.getresponse()
        getcontent = str(r.read(15))
    finally:
        if getcontent.find("DOCTYPE") != -1:
            print(ip + " [OK]")
        else:
            print(ip + " [ERROR]")
if __name__=="__main__":
 #   print(__name__)
    if get_iplist(domain) and len(iplist)>0:
        for ip in iplist:
            checkip(ip)
    else:
        print("02 dns resolver error")
