os_obfuscation_instr = """
RUN rm /etc/os-release
RUN rm /etc/debconf.conf
RUN rm /etc/debian_version
RUN rm /usr/lib/os-release
"""

ospkg_obfuscation_instr = """
RUN rm -rf var/lib/dpkg/
RUN rm -rf /var/cache/apt/archives/
RUN rm -rf /var/lib/apt/lists/
RUN rm -rf /usr/share/doc/
"""

default_install = """
WORKDIR /app
COPY requirements.txt .
RUN pip install --break-system-package -r requirements.txt
COPY . .
"""


python_pkg_obfuscation_instr = """
RUN rm -rf /usr/local/lib/python3.10/site-packages/*.dist-info
RUN rm -rf /usr/lib/python3/dist-packages/*.egg-info
"""

url_obfuscation_instr = """
RUN curl -o postgres.tar.gz -sSL "https://ftp.postgresql.org/pub/source/v16.3/postgresql-16.3.tar.gz"
"""

## CONTAINERS

base = lambda baseimg: f"""
FROM {baseimg}
{default_install}
"""

############# SINGLE OBFUSCATION ###############

url_obfuscation = lambda baseimg: f"""
FROM {baseimg}
{url_obfuscation_instr}
{default_install}
"""

os_obfuscation = lambda baseimg: f"""
FROM {baseimg}

{os_obfuscation_instr}

{default_install}

"""


pkg_obfuscation = lambda baseimg: f"""
FROM {baseimg}

{default_install}
{python_pkg_obfuscation_instr}
"""


dep_obfuscation = lambda baseimg: f"""
FROM {baseimg}

{default_install}

RUN rm requirements.txt
"""


link_obfuscation = lambda baseimg: f"""
FROM {baseimg}

RUN mv /usr/bin/openssl /file.txt
RUN ln -s /file.txt /usr/bin/openssl

{default_install}
"""


alias_obfuscation = lambda baseimg: f"""
FROM {baseimg}

RUN mv /usr/bin/openssl /file.txt
RUN echo "alias openssl='/file.txt'" >> /etc/bash.bashrc

{default_install}
"""


ospkg_obfuscation = lambda baseimg: f"""
FROM {baseimg}

{ospkg_obfuscation_instr}

{default_install}

"""

compress_obfuscation = lambda baseimg: f"""
FROM {baseimg} AS builder
{default_install}

FROM scratch
COPY --from=builder / /
WORKDIR /app
"""

############# DOUBLE OBFUSCATION ###############

os_pkg_obfuscation = lambda baseimg: f"""
FROM {baseimg}

{os_obfuscation_instr}

{default_install}
{python_pkg_obfuscation_instr}
"""


os_ospkg_obfuscation = lambda baseimg: f"""
FROM {baseimg}

{os_obfuscation_instr}

{ospkg_obfuscation_instr}

{default_install}
"""


os_pkg_obfuscation = lambda baseimg: f"""
FROM {baseimg}

{os_obfuscation_instr}

{default_install}
{python_pkg_obfuscation_instr}
"""


dep_pkg_obfuscation = lambda baseimg: f"""
FROM {baseimg}


{default_install}
{python_pkg_obfuscation_instr}
RUN rm requirements.txt

"""


os_dep_obfuscation = lambda baseimg: f"""
FROM {baseimg}

{os_obfuscation_instr}

{default_install}
RUN rm requirements.txt

"""
############# TRIPLE OBFUSCATION ###############

os_ospkg_dep_obfuscation = lambda baseimg: f"""
FROM {baseimg}

{os_obfuscation_instr}

{ospkg_obfuscation_instr}

{default_install}

RUN rm requirements.txt
"""


os_ospkg_pkg_obfuscation = lambda baseimg: f"""
FROM {baseimg}

{os_obfuscation_instr}

{ospkg_obfuscation_instr}

{default_install}

{python_pkg_obfuscation_instr}

"""

############# 4 OBFUSCATIONS ###############

os_ospkg_dep_pkg_obfuscation = lambda baseimg: f"""
FROM {baseimg}

{os_obfuscation_instr}

{ospkg_obfuscation_instr}

{default_install}

{python_pkg_obfuscation_instr}

RUN rm requirements.txt
"""

os_ospkg_dep_link_obfuscation = lambda baseimg: f"""
FROM {baseimg}

{os_obfuscation_instr}

{ospkg_obfuscation_instr}

RUN mv /usr/bin/openssl /file.txt
RUN ln -s /file.txt /usr/bin/openssl

{default_install}
RUN rm requirements.txt
"""

os_ospkg_dep_pack_obfuscation = lambda baseimg: f"""
FROM {baseimg} AS builder

{os_obfuscation_instr}

{ospkg_obfuscation_instr}

{default_install}

RUN rm requirements.txt

FROM scratch
COPY --from=builder / /
WORKDIR /app
"""

os_ospkg_pack_obfuscation = lambda baseimg: f"""
FROM {baseimg} AS builder

{os_obfuscation_instr}

{ospkg_obfuscation_instr}

{default_install}

FROM scratch
COPY --from=builder / /
WORKDIR /app
"""

os_ospkg_dep_alias_obfuscation = lambda baseimg: f"""
FROM {baseimg}

{os_obfuscation_instr}

{ospkg_obfuscation_instr}

RUN mv /usr/bin/openssl /file.txt
RUN echo "alias openssl='/file.txt'" >> /etc/bash.bashrc

{default_install}
RUN rm requirements.txt
"""

############# 5+ OBFUSCATIONS ###############

os_ospkg_dep_alias_pkg_obfuscation = lambda baseimg: f"""
FROM {baseimg}

{os_obfuscation_instr}

{ospkg_obfuscation_instr}

RUN mv /usr/bin/openssl /file.txt
RUN echo "alias openssl='/file.txt'" >> /etc/bash.bashrc

{default_install}
RUN rm requirements.txt
{python_pkg_obfuscation_instr}
"""

os_ospkg_dep_alias_pack_obfuscation = lambda baseimg: f"""
FROM {baseimg} AS builder

{os_obfuscation_instr}

{ospkg_obfuscation_instr}

RUN mv /usr/bin/openssl /file.txt
RUN echo "alias openssl='/file.txt'" >> /etc/bash.bashrc

{default_install}
RUN rm requirements.txt

FROM scratch
COPY --from=builder / /
WORKDIR /app
"""
