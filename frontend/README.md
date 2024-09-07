<br><br>
## Run the app

```
yarn install

yarn dev
```

## Config OpenAI and Azure TTS

```
add a .env file under frontend/ folder

in the .env file, add parameters` VITE_OPENAI_API_KEY`, `VITE_TTS_KEY` and `VITE_TTS_REGION` with your own keys

yarn dev
```

## Image build

1. Build the development environment image:

   ```
   docker-compose build dev
   ```

2. Start the development environment:

   ```
   docker-compose up dev
   ```

3. Build the production environment image:

   ```
   docker-compose build app
   ```

4. Start the production environment:
   ```
   docker-compose up app
   ```
