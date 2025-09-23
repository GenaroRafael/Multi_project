# CODNET

Sistema modular para la gestión de usuarios, contratos y pagos, con integración de servicios y microservicios.

##  Arquitectura General

El proyecto sigue un enfoque **monorepo modular** con separación en múltiples repositorios específicos:

- **CODNET** → Repositorio principal del sistema.
- **Utils** → Módulos comunes y modelos base (Usuario, Contrato, Pago, etc.).
- **Servicios** → Microservicios independientes que consumen Utils.
- **Block-COD** → Módulo de lógica de negocio específico (pendiente de definir).
- **CODNET-system** → Scripts y orquestación general (Docker, CI/CD, despliegues).

La arquitectura general está basada en:
- **Docker + Docker Compose** → Orquestación de servicios.
- **Python (Poetry)** → Gestión de dependencias.
- **MongoDB** → Base de datos principal.
- **Airflow** → Orquestación de flujos de datos.

## 📂 Convenciones de Carpetas

Ejemplo de estructura inicial:

CODNET/
├── utils/ # Repositorio de utilidades y modelos
│ ├── pyproject.toml
│ ├── utils/
│ │ ├── models/
│ │ │ ├── usuario.py
│ │ │ ├── contrato.py
│ │ │ └── pago.py
│ │ └── init.py
│ └── tests/
│
├── servicios/ # Microservicios
│ ├── servicio_a/
│ │ ├── pyproject.toml
│ │ ├── main.py
│ │ └── tests/
│ └── servicio_b/
│
├── airflow/ # Configuración de Airflow
│ ├── dags/
│ ├── Dockerfile
│ ├── docker-compose.yml
│ └── pyproject.toml
│
├── docker/ # Configuración general de Docker
│ ├── docker-compose.override.yml
│ └── .env.example
│
└── README.md


## 📌 Convenciones

- **Lenguaje**: Python 3.11+
- **Estilo de código**: [PEP8](https://peps.python.org/pep-0008/) + `black` + `isort`
- **Dependencias**: Gestionadas con **Poetry** en cada módulo.
- **Tests**: Carpeta `tests/` en cada repositorio/módulo.
- **Commits**: Estilo [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/).

## ✅ Próximos Pasos

- [ ] Crear script inicial en Python para probar conexión a MongoDB.
- [ ] Añadir `pyproject.toml` en todos los repos.
- [ ] Definir flujo de CI/CD inicial (GitHub Actions).
