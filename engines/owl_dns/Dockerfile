FROM alpine:latest
MAINTAINER Patrowl.io "getsupport@patrowl.io"
LABEL Name="Patrowl\ DNS\ \(Patrowl engine\)" Version="1.0.0"

# Install dependencies
RUN apk add --update \
    python \
    python-dev \
    py-pip \
    git \
  && rm -rf /var/cache/apk/*

# Create the target repo
RUN mkdir -p /opt/patrowl-engines/owl_dns
RUN mkdir -p /opt/patrowl-engines/owl_dns/results
RUN mkdir -p /opt/patrowl-engines/owl_dns/libs

# Set the working directory to /opt/<engine_name>
WORKDIR /opt/patrowl-engines/owl_dns

# Copy the current directory contents into the container at /
COPY __init__.py .
COPY engine-owl_dns.py .
COPY owl_dns.json.sample owl_dns.json
COPY requirements.txt .
COPY README.md .
COPY etc/ etc/
#COPY libs/python-whois/ libs/python-whois/
#COPY libs/Sublist3r/ libs/Sublist3r/
WORKDIR /opt/patrowl-engines/owl_dns/libs
RUN git clone https://github.com/aboul3la/Sublist3r
RUN git clone https://github.com/joepie91/python-whois

# Install python modules
WORKDIR /opt/patrowl-engines/owl_dns
RUN pip install --upgrade pip
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# TCP port exposed by the container (NAT)
EXPOSE 5006

# Run app.py when the container launches
CMD ["gunicorn", "engine-owl_dns:app", "-b", "0.0.0.0:5006"]
