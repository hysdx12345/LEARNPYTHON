class HtmlOutputer(object):
    def __init__(self):
        self.datas=[]
    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout=open('output.html','w')

        fout.write("<!DOCTYPE HTML>")
        fout.write("<html>")

        fout.write("<head>")
        fout.write("<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\">")
        fout.write("<title>")
        fout.write("My First Spider")
        fout.write("</title>")
        fout.write("</head>")

        fout.write("<body>")
        fout.write("<table>")

        fout.write("<tr>")
        fout.write("<td>标题</td>" )
        fout.write("<td>简介</td>")
        fout.write("</tr>")

        #ascii

        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td><a href=\"%s\">%s</a></td>" % (data['url'],data['title']))
            fout.write("<td>%s</td>" % data['summary'])
            fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")