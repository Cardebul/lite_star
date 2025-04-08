# litestar database make-migrations -m name

litestar database upgrade --no-prompt
litestar run -H 0.0.0.0 -p 8000