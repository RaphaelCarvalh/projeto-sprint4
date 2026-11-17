# Painel de Anúncios de Vendas de Carros

Aplicativo web feito com **Streamlit** para explorar um conjunto de dados de anúncios de venda de carros usados nos EUA (`vehicles_us.csv`). Os gráficos são interativos e gerados com **Plotly Express**.

## Para que serve

Com o aplicativo, você pode analisar visualmente os anúncios de carros. Por exemplo, dá para ver como a quilometragem dos veículos se distribui e qual é a relação entre a quilometragem e o preço.

## Funcionalidades

- **Histograma da quilometragem**: ao marcar a caixa *Criar um histograma*, o app mostra a distribuição da coluna `odometer`.
- **Gráfico de dispersão**: ao marcar a caixa *Criar um gráfico de dispersão*, o app mostra a relação entre quilometragem (`odometer`) e preço (`price`).
- As duas caixas podem ser marcadas ao mesmo tempo para ver os dois gráficos juntos.
- Os gráficos são interativos: dá para dar zoom, passar o mouse sobre os pontos e filtrar.

## Tecnologias

- Python
- pandas
- plotly-express
- streamlit

## Como executar localmente

```bash
pip install -r requirements.txt
streamlit run app.py
```

Depois, abra no navegador o endereço que aparecer no terminal.

## Deploy no Render

O arquivo `.streamlit/config.toml` configura o Streamlit para rodar no Render (modo headless e porta 10000).
