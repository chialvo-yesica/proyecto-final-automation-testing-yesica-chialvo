from typing import Any, Dict, Optional, List, Union
import requests
from requests import Response
from config.settings import BASE_URL_API_SERVICE

#Cliente simple para consumir APIs REST.
class RestApiClient:

    def __init__(self, base_url: str = BASE_URL_API_SERVICE):
        # Asegurar que no haya '/' duplicadas al final
        self.base_uri = base_url.rstrip("/")

    #Construye URL completa a partir de la ruta relativa
    def _build_full_path(self, relative_path: str) -> str:
        return f"{self.base_uri}/{relative_path.lstrip('/')}"

    # Ejecuta una petición GET al endpoint especificado
    def execute_get(self, path: str, query_params: Optional[Dict[str, Any]] = None, **extra_args) -> Response:
        full_url = self._build_full_path(path)
        return requests.get(full_url, params=query_params, **extra_args)

    #Ejecuta una petición POST al endpoint especificado
    def execute_post(
        self,
        path: str,
        body: Optional[Union[Dict[str, Any], List[Dict[str, Any]]]] = None,
        raw_data: Optional[Dict[str, Any]] = None,
        **extra_args,
    ) -> Response:
        full_url = self._build_full_path(path)
        return requests.post(full_url, json=body, data=raw_data, **extra_args)

    #Ejecuta una petición DELETE al endpoint especificado
    def execute_delete(self, path: str, **extra_args) -> Response:
        full_url = self._build_full_path(path)
        return requests.delete(full_url, **extra_args)