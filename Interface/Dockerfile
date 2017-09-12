FROM django:onbuild
COPY entrypoint.sh entrypoint.sh
EXPOSE 8000
RUN chmod +x entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]