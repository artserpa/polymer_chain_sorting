


```bash
montecarlo-sorting-analysis/
├── main.py                        # Script principal para rodar o fluxo completo
├── requirements.txt               # Dependências do projeto
├── README.md                      # Descrição do projeto
├── data/                          # (opcional) Dados de entrada/saída se quiser salvar algo
│   ├── raw/                       # Dados brutos (se necessário)
│   └── processed/                 # Resultados tratados
├── results/                       # Saída de gráficos, tabelas, logs
├── montecarlo/                    # Pacote principal com códigos
│   ├── __init__.py
│   ├── simulation.py              # Funções e classes para gerar as cadeias MC
│   ├── sorting_algorithms.py      # Implementações de bubble, insertion, selection, timsort
│   ├── analysis.py                 # Funções de pós-processamento e métricas de eficiência
│   └── visualization.py           # Funções para gerar gráficos
├── tests/                         # Testes unitários
│   ├── __init__.py
│   ├── test_simulation.py
│   ├── test_sorting_algorithms.py
│   └── test_analysis.py
└── docs/                          # Documentação mais detalhada (ex: metodologia, exemplos)
    └── methodology.md
``