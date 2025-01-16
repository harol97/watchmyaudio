type SuccessResponse<T> = {
  status: "success";
  message: string;
  statusCode: number;
  data: T;
};

type FetchError = {
  status: "error";
  message: string;
  statusCode: number;
};
type NetworkError = {
  status: "netWorkError";
  message: string;
  statusCode: number;
};

type Response<T> = SuccessResponse<T> | FetchError | NetworkError;

export default async function baseFetch<T>(endpoint: string, options: RequestInit = {}): Promise<Response<T>> {
  const messageError = "Hubo un error en la aplicación. Vuelva intentarlo más tarde";
  const messageOk = "Se ha realizado la tarea con éxito";
  try {
    const base_url = process.env.BASE_URL;
    const url = `${base_url}${endpoint}`;

    const response = await fetch(url, options);
    const statusCode = response.status;
    try {
      const data = await response.json();
      if (response.ok)
        return {
          status: "success",
          message: data.mensaje ?? data.message ?? messageOk,
          statusCode: statusCode,
          data: data,
        };
      return {
        status: "error",
        message: data.mensaje ?? JSON.stringify(data.detail) ?? data.message ?? messageError,
        statusCode,
      };
    } catch {
      return { status: "error", message: messageError, statusCode };
    }
  } catch {
    return { status: "netWorkError", message: "Problema de Red", statusCode: -1 };
  }
}
