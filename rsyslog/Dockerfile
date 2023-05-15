FROM debian:latest


RUN apt-get update
RUN apt-get install --no-install-recommends -y rsyslog
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/*

COPY rsyslog.conf /rsyslog.conf/etc/rsyslog.conf

ENTRYPOINT ["rsyslogd", "-n"]