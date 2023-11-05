FROM alpine
RUN apk update && apk add bash curl
WORKDIR /app
RUN curl -s https://i.jpillora.com/installer | bash
EXPOSE 3003
CMD /app/installer
