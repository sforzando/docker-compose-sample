# docker-compose-sample

![docker-compose Sample CI](https://github.com/sforzando/docker-compose-sample/workflows/docker-compose%20Sample%20CI/badge.svg)

- [Run](#run)
- [Stop](#stop)
- [Check](#check)
  - [Web](#web)
  - [Tor](#tor)
- [Clearance](#clearance)
  - [Prune Containers and Volumes](#prune-containers-and-volumes)
  - [Remove Images](#remove-images)
- [Misc](#misc)
  - [License](#license)
  - [Author](#author)

## Run

```shell
$ docker-compose up --build --force-recreate

Creating network "docker-compose-sample_default" with the default driver
Building web
Step 1/5 : FROM python:3
3: Pulling from library/python
e9afc4f90ab0: Pull complete
989e6b19a265: Pull complete
af14b6c2f878: Pull complete
5573c4b30949: Pull complete
11a88e764313: Pull complete
ee776f0e36af: Pull complete
513c90a1afc3: Pull complete
df9b9e95bdb9: Pull complete
86c9edb54464: Pull complete
Digest: sha256:dd6cd8191ccbced2a6af5d0ddb51e6057c1444df14e14bcfd5c7b3ef78738050
Status: Downloaded newer image for python:3
 ---> 7f5b6ccd03e9
Step 2/5 : ADD . /code
 ---> 56b760a96007
Step 3/5 : WORKDIR /code
 ---> Running in 7f07492c74c3
Removing intermediate container 7f07492c74c3
 ---> 24c794cefe7e
Step 4/5 : RUN pip install -r requirements.txt
 ---> Running in eb966f57ead1
Collecting flask
  Downloading Flask-1.1.2-py2.py3-none-any.whl (94 kB)
Collecting google-api-python-client
  Downloading google_api_python_client-1.9.3-py3-none-any.whl (59 kB)
Collecting luigi
  Downloading luigi-3.0.0.tar.gz (1.2 MB)
Collecting pandas
  Downloading pandas-1.0.5-cp38-cp38-manylinux1_x86_64.whl (10.0 MB)
Collecting redis
  Downloading redis-3.5.3-py2.py3-none-any.whl (72 kB)
Collecting Scrapy
  Downloading Scrapy-2.1.0-py2.py3-none-any.whl (239 kB)
Collecting selenium
  Downloading selenium-3.141.0-py2.py3-none-any.whl (904 kB)
Collecting Jinja2>=2.10.1
  Downloading Jinja2-2.11.2-py2.py3-none-any.whl (125 kB)
Collecting itsdangerous>=0.24
  Downloading itsdangerous-1.1.0-py2.py3-none-any.whl (16 kB)
Collecting Werkzeug>=0.15
  Downloading Werkzeug-1.0.1-py2.py3-none-any.whl (298 kB)
Collecting click>=5.1
  Downloading click-7.1.2-py2.py3-none-any.whl (82 kB)
Collecting httplib2<1dev,>=0.9.2
  Downloading httplib2-0.18.1-py3-none-any.whl (95 kB)
Collecting google-auth>=1.16.0
  Downloading google_auth-1.18.0-py2.py3-none-any.whl (90 kB)
Collecting uritemplate<4dev,>=3.0.0
  Downloading uritemplate-3.0.1-py2.py3-none-any.whl (15 kB)
Collecting google-api-core<2dev,>=1.18.0
  Downloading google_api_core-1.21.0-py2.py3-none-any.whl (90 kB)
Collecting google-auth-httplib2>=0.0.3
  Downloading google_auth_httplib2-0.0.3-py2.py3-none-any.whl (6.3 kB)
Collecting six<2dev,>=1.6.1
  Downloading six-1.15.0-py2.py3-none-any.whl (10 kB)
Collecting python-dateutil<3,>=2.7.5
  Downloading python_dateutil-2.8.1-py2.py3-none-any.whl (227 kB)
Collecting python-daemon
  Downloading python_daemon-2.2.4-py2.py3-none-any.whl (35 kB)
Collecting tornado<6,>=4.0
  Downloading tornado-5.1.1.tar.gz (516 kB)
Collecting numpy>=1.13.3
  Downloading numpy-1.19.0-cp38-cp38-manylinux2010_x86_64.whl (14.6 MB)
Collecting pytz>=2017.2
  Downloading pytz-2020.1-py2.py3-none-any.whl (510 kB)
Collecting pyOpenSSL>=16.2.0
  Downloading pyOpenSSL-19.1.0-py2.py3-none-any.whl (53 kB)
Collecting protego>=0.1.15
  Downloading Protego-0.1.16.tar.gz (3.2 MB)
Collecting Twisted>=17.9.0
  Downloading Twisted-20.3.0.tar.bz2 (3.1 MB)
Collecting lxml>=3.5.0
  Downloading lxml-4.5.1-cp38-cp38-manylinux1_x86_64.whl (5.4 MB)
Collecting w3lib>=1.17.0
  Downloading w3lib-1.22.0-py2.py3-none-any.whl (20 kB)
Collecting PyDispatcher>=2.0.5
  Downloading PyDispatcher-2.0.5.tar.gz (34 kB)
Collecting cssselect>=0.9.1
  Downloading cssselect-1.1.0-py2.py3-none-any.whl (16 kB)
Collecting parsel>=1.5.0
  Downloading parsel-1.6.0-py2.py3-none-any.whl (13 kB)
Collecting service-identity>=16.0.0
  Downloading service_identity-18.1.0-py2.py3-none-any.whl (11 kB)
Collecting cryptography>=2.0
  Downloading cryptography-2.9.2-cp35-abi3-manylinux2010_x86_64.whl (2.7 MB)
Collecting queuelib>=1.4.2
  Downloading queuelib-1.5.0-py2.py3-none-any.whl (13 kB)
Collecting zope.interface>=4.1.3
  Downloading zope.interface-5.1.0-cp38-cp38-manylinux2010_x86_64.whl (243 kB)
Collecting urllib3
  Downloading urllib3-1.25.9-py2.py3-none-any.whl (126 kB)
Collecting MarkupSafe>=0.23
  Downloading MarkupSafe-1.1.1-cp38-cp38-manylinux1_x86_64.whl (32 kB)
Collecting pyasn1-modules>=0.2.1
  Downloading pyasn1_modules-0.2.8-py2.py3-none-any.whl (155 kB)
Collecting rsa<5,>=3.1.4; python_version >= "3"
  Downloading rsa-4.6-py3-none-any.whl (47 kB)
Collecting cachetools<5.0,>=2.0.0
  Downloading cachetools-4.1.0-py3-none-any.whl (10 kB)
Requirement already satisfied: setuptools>=40.3.0 in /usr/local/lib/python3.8/site-packages (from google-auth>=1.16.0->google-api-python-client->-r requirements.txt (line 2)) (47.1.1)
Collecting protobuf>=3.12.0
  Downloading protobuf-3.12.2-cp38-cp38-manylinux1_x86_64.whl (1.3 MB)
Collecting googleapis-common-protos<2.0dev,>=1.6.0
  Downloading googleapis_common_protos-1.52.0-py2.py3-none-any.whl (100 kB)
Collecting requests<3.0.0dev,>=2.18.0
  Downloading requests-2.24.0-py2.py3-none-any.whl (61 kB)
Collecting docutils
  Downloading docutils-0.16-py2.py3-none-any.whl (548 kB)
Collecting lockfile>=0.10
  Downloading lockfile-0.12.2-py2.py3-none-any.whl (13 kB)
Collecting constantly>=15.1
  Downloading constantly-15.1.0-py2.py3-none-any.whl (7.9 kB)
Collecting incremental>=16.10.1
  Using cached incremental-17.5.0-py2.py3-none-any.whl (16 kB)
Collecting Automat>=0.3.0
  Downloading Automat-20.2.0-py2.py3-none-any.whl (31 kB)
Collecting hyperlink>=17.1.1
  Downloading hyperlink-19.0.0-py2.py3-none-any.whl (38 kB)
Collecting PyHamcrest!=1.10.0,>=1.9.0
  Downloading PyHamcrest-2.0.2-py3-none-any.whl (52 kB)
Collecting attrs>=19.2.0
  Downloading attrs-19.3.0-py2.py3-none-any.whl (39 kB)
Collecting pyasn1
  Downloading pyasn1-0.4.8-py2.py3-none-any.whl (77 kB)
Collecting cffi!=1.11.3,>=1.8
  Downloading cffi-1.14.0-cp38-cp38-manylinux1_x86_64.whl (409 kB)
Collecting chardet<4,>=3.0.2
  Downloading chardet-3.0.4-py2.py3-none-any.whl (133 kB)
Collecting idna<3,>=2.5
  Downloading idna-2.9-py2.py3-none-any.whl (58 kB)
Collecting certifi>=2017.4.17
  Downloading certifi-2020.6.20-py2.py3-none-any.whl (156 kB)
Collecting pycparser
  Downloading pycparser-2.20-py2.py3-none-any.whl (112 kB)
Building wheels for collected packages: luigi, tornado, protego, Twisted, PyDispatcher
  Building wheel for luigi (setup.py): started
  Building wheel for luigi (setup.py): finished with status 'done'
  Created wheel for luigi: filename=luigi-3.0.0-py3-none-any.whl size=1076781 sha256=ab7b9b8eee6b261385df07f20cd5acb17e679880ffad464ded2b648d76b6fe9b
  Stored in directory: /root/.cache/pip/wheels/69/6a/b4/197aa47660a8d865aad027dde5101217e5687c81dff99e8570
  Building wheel for tornado (setup.py): started
  Building wheel for tornado (setup.py): finished with status 'done'
  Created wheel for tornado: filename=tornado-5.1.1-cp38-cp38-linux_x86_64.whl size=462505 sha256=02a12e27fef5b3788e8fc540bccadcafc1ffeba51038a8878ea12f78ee1a5b23
  Stored in directory: /root/.cache/pip/wheels/25/a1/e3/b0d37c6c451fc21f290cf026f6352382e6cbced32dc3f6a37a
  Building wheel for protego (setup.py): started
  Building wheel for protego (setup.py): finished with status 'done'
  Created wheel for protego: filename=Protego-0.1.16-py3-none-any.whl size=7765 sha256=a5d5b27ef6ff0da99e9ae8c53fac438534ec861091cca8c56ae76aec98cffd5a
  Stored in directory: /root/.cache/pip/wheels/91/64/36/bd0d11306cb22a78c7f53d603c7eb74ebb6c211703bc40b686
  Building wheel for Twisted (setup.py): started
  Building wheel for Twisted (setup.py): finished with status 'done'
  Created wheel for Twisted: filename=Twisted-20.3.0-cp38-cp38-linux_x86_64.whl size=3087606 sha256=768f4ee92a5495b0df775266cae7d7e981f25abe158ca94121986bb1f0132c4f
  Stored in directory: /root/.cache/pip/wheels/f2/36/1b/99fe6d339e1559e421556c69ad7bc8c869145e86a756c403f4
  Building wheel for PyDispatcher (setup.py): started
  Building wheel for PyDispatcher (setup.py): finished with status 'done'
  Created wheel for PyDispatcher: filename=PyDispatcher-2.0.5-py3-none-any.whl size=11515 sha256=90840a480195b14ffb8806656f9646a6805abaac8163f279eb04c7fc005369f5
  Stored in directory: /root/.cache/pip/wheels/d1/d7/61/11b5b370ee487d38b5408ecb7e0257db9107fa622412cbe2ff
Successfully built luigi tornado protego Twisted PyDispatcher
Installing collected packages: MarkupSafe, Jinja2, itsdangerous, Werkzeug, click, flask, httplib2, six, pyasn1, pyasn1-modules, rsa, cachetools, google-auth, uritemplate, pytz, protobuf, googleapis-common-protos, chardet, idna, urllib3, certifi, requests, google-api-core, google-auth-httplib2, google-api-python-client, python-dateutil, docutils, lockfile, python-daemon, tornado, luigi, numpy, pandas, redis, pycparser, cffi, cryptography, pyOpenSSL, protego, zope.interface, constantly, incremental, attrs, Automat, hyperlink, PyHamcrest, Twisted, lxml, w3lib, PyDispatcher, cssselect, parsel, service-identity, queuelib, Scrapy, selenium
Successfully installed Automat-20.2.0 Jinja2-2.11.2 MarkupSafe-1.1.1 PyDispatcher-2.0.5 PyHamcrest-2.0.2 Scrapy-2.1.0 Twisted-20.3.0 Werkzeug-1.0.1 attrs-19.3.0 cachetools-4.1.0 certifi-2020.6.20 cffi-1.14.0 chardet-3.0.4 click-7.1.2 constantly-15.1.0 cryptography-2.9.2 cssselect-1.1.0 docutils-0.16 flask-1.1.2 google-api-core-1.21.0 google-api-python-client-1.9.3 google-auth-1.18.0 google-auth-httplib2-0.0.3 googleapis-common-protos-1.52.0 httplib2-0.18.1 hyperlink-19.0.0 idna-2.9 incremental-17.5.0 itsdangerous-1.1.0 lockfile-0.12.2 luigi-3.0.0 lxml-4.5.1 numpy-1.19.0 pandas-1.0.5 parsel-1.6.0 protego-0.1.16 protobuf-3.12.2 pyOpenSSL-19.1.0 pyasn1-0.4.8 pyasn1-modules-0.2.8 pycparser-2.20 python-daemon-2.2.4 python-dateutil-2.8.1 pytz-2020.1 queuelib-1.5.0 redis-3.5.3 requests-2.24.0 rsa-4.6 selenium-3.141.0 service-identity-18.1.0 six-1.15.0 tornado-5.1.1 uritemplate-3.0.1 urllib3-1.25.9 w3lib-1.22.0 zope.interface-5.1.0
Removing intermediate container eb966f57ead1
 ---> 61cd67ff44b3
Step 5/5 : CMD ["python", "app.py"]
 ---> Running in 9cbae243732f
Removing intermediate container 9cbae243732f
 ---> fb3add2ee3d8
Successfully built fb3add2ee3d8
Successfully tagged docker-compose-sample_web:latest
Pulling redis (redis:latest)...
latest: Pulling from library/redis
8559a31e96f4: Pull complete
85a6a5c53ff0: Pull complete
b69876b7abed: Pull complete
a72d84b9df6a: Pull complete
5ce7b314b19c: Pull complete
04c4bfb0b023: Pull complete
Digest: sha256:800f2587bf3376cb01e6307afe599ddce9439deafbd4fb8562829da96085c9c5
Status: Downloaded newer image for redis:latest
Pulling tor (dperson/torproxy:)...
latest: Pulling from dperson/torproxy
cbdbe7a5bc2a: Pull complete
2c55062ae548: Pull complete
f3fc136a14ff: Pull complete
Digest: sha256:f7317fad57d357f0bf4b1f2e9a5637fd3467a96d9fce284bbe69f6926cbd82b2
Status: Downloaded newer image for dperson/torproxy:latest
Creating docker-compose-sample_web_1   ... done
Creating docker-compose-sample_redis_1 ... done
Creating docker-compose-sample_tor_1   ... done
Attaching to docker-compose-sample_redis_1, docker-compose-sample_tor_1, docker-compose-sample_web_1
redis_1  | 1:C 24 Jun 2020 08:53:54.318 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
redis_1  | 1:C 24 Jun 2020 08:53:54.318 # Redis version=6.0.5, bits=64, commit=00000000, modified=0, pid=1, just started
redis_1  | 1:C 24 Jun 2020 08:53:54.318 # Warning: no config file specified, using the default config. In order to specify a config file use redis-server /path/to/redis.conf
redis_1  | 1:M 24 Jun 2020 08:53:54.327 * Running mode=standalone, port=6379.
redis_1  | 1:M 24 Jun 2020 08:53:54.327 # WARNING: The TCP backlog setting of 511 cannot be enforced because /proc/sys/net/core/somaxconn is set to the lower value of 128.
redis_1  | 1:M 24 Jun 2020 08:53:54.327 # Server initialized
redis_1  | 1:M 24 Jun 2020 08:53:54.327 # WARNING you have Transparent Huge Pages (THP) support enabled in your kernel. This will create latency and memory usage issues with Redis. To fix this issue run the command 'echo never > /sys/kernel/mm/transparent_hugepage/enabled' as root, and add it to your /etc/rc.local in order to retain the setting after a reboot. Redis must be restarted after THP is disabled.
redis_1  | 1:M 24 Jun 2020 08:53:54.328 * Ready to accept connections
web_1    |  * Serving Flask app "app" (lazy loading)
web_1    |  * Environment: production
web_1    |    WARNING: This is a development server. Do not use it in a production deployment.
web_1    |    Use a production WSGI server instead.
web_1    |  * Debug mode: on
web_1    |  * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
web_1    |  * Restarting with stat
web_1    |  * Debugger is active!
web_1    |  * Debugger PIN: 112-162-339
tor_1    | Jun 24 08:53:55.351 [notice] Tor 0.4.1.9 running on Linux with Libevent 2.1.11-stable, OpenSSL 1.1.1g, Zlib 1.2.11, Liblzma N/A, and Libzstd N/A.
tor_1    | Jun 24 08:53:55.351 [notice] Tor can't help you if you use it wrong! Learn how to be safe at https://www.torproject.org/download/download#warning
tor_1    | Jun 24 08:53:55.351 [notice] Read configuration file "/etc/tor/torrc".
tor_1    | Jun 24 08:53:55.355 [warn] You specified a public address '0.0.0.0:9040' for TransPort. Other people on the Internet might find your computer and use it as an open proxy. Please don't allow this unless you have a good reason.
tor_1    | Jun 24 08:53:55.356 [warn] You specified a public address '0.0.0.0:9050' for SocksPort. Other people on the Internet might find your computer and use it as an open proxy. Please don't allow this unless you have a good reason.
tor_1    | Jun 24 08:53:55.356 [warn] You specified a public address '0.0.0.0:9040' for TransPort. Other people on the Internet might find your computer and use it as an open proxy. Please don't allow this unless you have a good reason.
tor_1    | Jun 24 08:53:55.356 [notice] Opening Socks listener on 0.0.0.0:9050
tor_1    | Jun 24 08:53:55.356 [notice] Opened Socks listener on 0.0.0.0:9050
tor_1    | Jun 24 08:53:55.356 [notice] Opening DNS listener on 127.0.0.1:5353
tor_1    | Jun 24 08:53:55.356 [notice] Opened DNS listener on 127.0.0.1:5353
tor_1    | Jun 24 08:53:55.356 [notice] Opening Transparent pf/netfilter listener on 0.0.0.0:9040
tor_1    | Jun 24 08:53:55.356 [notice] Opened Transparent pf/netfilter listener on 0.0.0.0:9040
tor_1    | Jun 24 08:53:55.356 [notice] Opening Control listener on 127.0.0.1:9051
tor_1    | Jun 24 08:53:55.356 [notice] Opened Control listener on 127.0.0.1:9051
tor_1    | Jun 24 08:53:55.356 [warn] Fixing permissions on directory /var/lib/tor
tor_1    | Jun 24 08:53:55.000 [notice] Parsing GEOIP IPv4 file /usr/share/tor/geoip.
tor_1    | Jun 24 08:53:55.000 [notice] Parsing GEOIP IPv6 file /usr/share/tor/geoip6.
tor_1    | Jun 24 08:53:55.000 [notice] Bootstrapped 0% (starting): Starting
tor_1    | Jun 24 08:53:55.000 [notice] Starting with guard context "default"
tor_1    | Jun 24 08:53:56.000 [notice] Opening Control listener on /etc/tor/run/control
tor_1    | Jun 24 08:53:56.000 [notice] Opened Control listener on /etc/tor/run/control
tor_1    | Jun 24 08:53:56.000 [notice] Bootstrapped 5% (conn): Connecting to a relay
tor_1    | Jun 24 08:53:56.000 [notice] Bootstrapped 10% (conn_done): Connected to a relay
tor_1    | Jun 24 08:53:57.000 [notice] Bootstrapped 14% (handshake): Handshaking with a relay
tor_1    | Jun 24 08:53:57.000 [notice] Bootstrapped 15% (handshake_done): Handshake with a relay done
tor_1    | Jun 24 08:53:57.000 [notice] Bootstrapped 20% (onehop_create): Establishing an encrypted directory connection
tor_1    | Jun 24 08:53:58.000 [notice] Bootstrapped 25% (requesting_status): Asking for networkstatus consensus
tor_1    | Jun 24 08:53:58.000 [notice] Bootstrapped 30% (loading_status): Loading networkstatus consensus
tor_1    | Jun 24 08:54:01.000 [notice] I learned some more directory information, but not enough to build a circuit: We have no usable consensus.
tor_1    | Jun 24 08:54:02.000 [notice] Bootstrapped 40% (loading_keys): Loading authority key certs
tor_1    | Jun 24 08:54:02.000 [notice] The current consensus has no exit nodes. Tor can only build internal paths, such as paths to onion services.
tor_1    | Jun 24 08:54:02.000 [notice] Bootstrapped 45% (requesting_descriptors): Asking for relay descriptors
tor_1    | Jun 24 08:54:02.000 [notice] I learned some more directory information, but not enough to build a circuit: We need more microdescriptors: we have 0/6144, and can only build 0% of likely paths. (We have 0% of guards bw, 0% of midpoint bw, and 0% of end bw (no exits in consensus, using mid) = 0% of path bw.)
tor_1    | Jun 24 08:54:03.000 [notice] Bootstrapped 50% (loading_descriptors): Loading relay descriptors
tor_1    | Jun 24 08:54:05.000 [notice] The current consensus contains exit nodes. Tor can build exit and internal paths.
tor_1    | Jun 24 08:54:06.000 [notice] Bootstrapped 55% (loading_descriptors): Loading relay descriptors
tor_1    | Jun 24 08:54:06.000 [notice] Bootstrapped 62% (loading_descriptors): Loading relay descriptors
tor_1    | Jun 24 08:54:06.000 [notice] Bootstrapped 67% (loading_descriptors): Loading relay descriptors
tor_1    | Jun 24 08:54:06.000 [notice] Bootstrapped 73% (loading_descriptors): Loading relay descriptors
tor_1    | Jun 24 08:54:06.000 [notice] Bootstrapped 75% (enough_dirinfo): Loaded enough directory info to build circuits
tor_1    | Jun 24 08:54:06.000 [notice] Bootstrapped 80% (ap_conn): Connecting to a relay to build circuits
tor_1    | Jun 24 08:54:06.000 [notice] Bootstrapped 85% (ap_conn_done): Connected to a relay to build circuits
tor_1    | Jun 24 08:54:07.000 [notice] Bootstrapped 89% (ap_handshake): Finishing handshake with a relay to build circuits
tor_1    | Jun 24 08:54:07.000 [notice] Bootstrapped 90% (ap_handshake_done): Handshake finished with a relay to build circuits
tor_1    | Jun 24 08:54:07.000 [notice] Bootstrapped 95% (circuit_create): Establishing a Tor circuit
tor_1    | Jun 24 08:54:08.000 [notice] Bootstrapped 100% (done): Done
```

## Stop

`Ctrl-C` to stop STDOUT logs.

```shell
$ docker-compose down --remove-orphans

Stopping docker-compose-sample_tor_1   ... done
Stopping docker-compose-sample_redis_1 ... done
Stopping docker-compose-sample_web_1   ... done
Removing docker-compose-sample_tor_1   ... done
Removing docker-compose-sample_redis_1 ... done
Removing docker-compose-sample_web_1   ... done
Removing network docker-compose-sample_default
```

## Check

### Web

And you will be able to see this web server running at `http://0.0.0.0:5000/` .

### Tor

cURL via Tor.

```shell
$ curl -sL inet-ip.info/json/indent

{
 "IP": "39.110.199.214",
 "Hostname": "[fs276ec7d6.knge101.ap.nuro.jp.]",
 "CountryCode": "JP",
 "CountryName": "Japan",
 "Accept": [
  "*/*"
 ],
 "AcceptEncoding": null,
 "AcceptLanguage": null,
 "UserAgent": [
  "curl/7.70.0"
 ],
 "Via": null,
 "XForwardedFor": [
  "39.110.199.214"
 ],
 "XForwardedPort": null,
 "XForwardedProto": [
  "http"
 ],
 "RequestURI": "/json/indent"
}

$ curl -SL --socks5 127.0.0.1:9050 inet-ip.info/json/indent

{
 "IP": "77.247.181.163",
 "Hostname": "[lumumba.torservers.net.]",
 "CountryCode": "NL",
 "CountryName": "Netherlands",
 "Accept": [
  "*/*"
 ],
 "AcceptEncoding": null,
 "AcceptLanguage": null,
 "UserAgent": [
  "curl/7.70.0"
 ],
 "Via": null,
 "XForwardedFor": [
  "77.247.181.163"
 ],
 "XForwardedPort": null,
 "XForwardedProto": [
  "http"
 ],
 "RequestURI": "/json/indent"
}
```

## Clearance

### Prune Containers and Volumes

```shell
$ docker system prune --volumes

WARNING! This will remove:
  - all stopped containers
  - all networks not used by at least one container
  - all volumes not used by at least one container
  - all dangling images
  - all dangling build cache

Are you sure you want to continue? [y/N] y
Deleted Volumes:
21e466d2c8f0a203a76c6f2cad1c29cdf0d13f0f0a661d6812c52774fa0dbf84
1b9ede7fc41924c6c70ef0b1fc1635a7699ba2fca22455a84c27ce4cfd1abcb8
7c39e9161f9eeaf32de74e7a415ae6bf422070edc3d7dff43878ea782e9f30c8

Total reclaimed space: 7.046MB
```

### Remove Images

```shell
$ docker rmi `docker images -q`

Untagged: docker-compose-sample_web:latest
Deleted: sha256:fb3add2ee3d8079d19059cc931c62d419413bf102a710b34671ab5c4ca415f96
Deleted: sha256:61cd67ff44b351b10404c71a474f9ff99ab507a5273c84f88bf3fba264004adf
Deleted: sha256:b02758c7293ecb95232f391a99166c1f437909eda1a6f5d20672c574a8d41c27
Deleted: sha256:24c794cefe7e4205e7b0831cc15fd9d07d323a70ac95761261114e48d83772cb
Deleted: sha256:56b760a96007af6f5b077afa923666b45f51e7914dfb74493071a69bae4f1737
Deleted: sha256:5b86f0108a1f0ea5a77b05fc2875a6c8a432bb5092a6d97fee97100768dd7fec
Untagged: redis:latest
Untagged: redis@sha256:800f2587bf3376cb01e6307afe599ddce9439deafbd4fb8562829da96085c9c5
Deleted: sha256:2355926154447ec75b25666ff5df14d1ab54f8bb4abf731be2fcb818c7a7f145
Deleted: sha256:852691351e76013456bccc5ca476ea5998cd4ef829ff88f36aa6152d26752a9f
Deleted: sha256:5638adc92bc136b5d1fa65b5eb75163949c27f9fc372c575ad840b07a19889af
Deleted: sha256:8e68e4829a31a04ca33cdab1c52f2e1dc34ff1eae8f858f87bdb97577e206230
Deleted: sha256:68d6751877f41a67f7fde5abb4c89d3b695df08603299fbf3585d6d1ff09a0e4
Deleted: sha256:7c2052306f31e2f3ba13c29dfff01ca66009d7d44917689662c6bc5ae1725e80
Deleted: sha256:13cb14c2acd34e45446a50af25cb05095a17624678dbafbcc9e26086547c1d74
Untagged: python:3
Untagged: python@sha256:dd6cd8191ccbced2a6af5d0ddb51e6057c1444df14e14bcfd5c7b3ef78738050
Deleted: sha256:7f5b6ccd03e9da5e02a20ea4377ae61f6ae1b935b05c1bd52fdafe4b958b5e50
Deleted: sha256:49088bdb2a7eaf5853ab71ccf0b87333a38232eee6bacd7466a96f4c8923082b
Deleted: sha256:40f4279dff1b6df4aa005d7fc2db1ded33a5b0b86ffbb5c285249fd94d178e64
Deleted: sha256:71d69e5c317de97a49a3dbea7a2cb8b6c1f494e8dc590a22198452ceb01a82e9
Deleted: sha256:394707a304bf9800c3a41e3e39c631a799a8b81cc2498ef7e9e0bcc92dadf3d9
Deleted: sha256:3338f00f687e1148db3db12c0c97bac53997c33a11cb71349a3e1e3c541f8717
Deleted: sha256:f863ffb247f4c239aeccf155b7c0d92e35403aed0c825690f6739a89a5901a7c
Deleted: sha256:d39c04f36d47ec7121d94577c33c2792aa6e5a5a2c1130ea0be67a96d4e42ba5
Deleted: sha256:7ef5d661de63acc27e877ff7098e93fd9d915f9688e8b585af1b3cccafd76243
Deleted: sha256:8803ef42039dcbe936755e9baae4bb7b19cb0fb6a438eb3992950cd0afef8e4f
Untagged: dperson/torproxy:latest
Untagged: dperson/torproxy@sha256:f7317fad57d357f0bf4b1f2e9a5637fd3467a96d9fce284bbe69f6926cbd82b2
Deleted: sha256:6ba4a6d10861385feb52c769558231e6a5a4d49826ec46a450a0794438148434
Deleted: sha256:eec9e6fd713a9608d5e6a59da7b7df661f465e3315cfc0df68f283aca6d26278
Deleted: sha256:c5614fbd58e225e07bd2cf212fa617380002021b4651154f9d9cb6ac2b2a971c
Deleted: sha256:3e207b409db364b595ba862cdc12be96dcdad8e36c59a03b7b3b61c946a5741a
```

## Misc

### License

[NYSL](http://www.kmonos.net/nysl/)

### Author

- [Shin'ichiro Suzuki](mailto:shin@sforzando.co.jp)
