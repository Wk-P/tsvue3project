export interface URL {
    proto: string;
    host: string;
    port: number;
    url: string;
    params: string;
};

export function initURL(url: URL): string {
    return `${url.proto}${url.host}:${url.port}${url.url}${url.params}`;
};


export interface Item {
    id: number;
    title: string;
    name: string;
    desc: string;
    price: number;
}

export interface User {
    id: number;
    username: string;
    status: string;
}

export interface UserLoginObj {
    username: string,
    password: string
}