from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>TCP/IP Protocol Table</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 40px;
      background-color: #f4f4f4;
    }
    h1 {
      text-align: center;
    }
    table {
      width: 80%;
      margin: auto;
      border-collapse: collapse;
      background-color: #fff;
    }
    th, td {
      border: 1px solid #ccc;
      padding: 12px;
      text-align: center;
    }
    th {
      background-color: #007BFF;
      color: white;
    }
    tr:nth-child(even) {
      background-color: #f2f2f2;
    }
  </style>
</head>
<body>
  <h1>TCP/IP Protocol Suite</h1>
  <table>
    <tr>
      <th>Layer</th>
      <th>Protocols</th>
      <th>Examples</th>
    </tr>
    <tr>
      <td>Application</td>
      <td>HTTP, FTP, SMTP, DNS</td>
      <td>Web browsing, Email, File transfer</td>
    </tr>
    <tr>
      <td>Transport</td>
      <td>TCP, UDP</td>
      <td>Reliable delivery, Streaming</td>
    </tr>
    <tr>
      <td>Internet</td>
      <td>IP, ICMP, ARP</td>
      <td>Routing, Addressing</td>
    </tr>
    <tr>
      <td>Network Access</td>
      <td>Ethernet, Wi-Fi</td>
      <td>Physical transmission</td>
    </tr>
  </table>
</body>
</html>

"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()