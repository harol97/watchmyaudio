export class ServerExepction extends Error {
    constructor(message: string) {
      super(message);
    }
  }
  
  export class FetchException extends Error {
    readonly statusCodeOwn: number;
  
    constructor(message: string, statusCode: number) {
      super(message, {
        cause: {
          type: "fetchError",
        },
      });
      this.statusCodeOwn = statusCode;
    }
  }
  
  export class NetworkException extends Error {
    constructor() {
      super("Error de Red");
    }
  }
  