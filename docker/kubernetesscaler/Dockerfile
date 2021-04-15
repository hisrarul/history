FROM python:3

RUN useradd -ms /bin/bash kubernetesscaler

USER kubernetesscaler

WORKDIR /home/kubernetesscaler
 
COPY --chown=kubernetesscaler:kubernetesscaler kubernetesscaler .

RUN pip3 install --user --no-cache-dir -r requirements.txt

ENTRYPOINT [ "python3", "scaler.py" ]

CMD ["--action", "up"]
