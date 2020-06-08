import * as axios from 'axios';
import { API } from './config';

const getBooks = async function () {
    try {
        const response = await axios.get(`${API}/books`)
        let data = parseList(response);
        return data;
    } catch (error) {
        console.error(error);
        return [];
    }
};

const deleteBook = async function (book) {
    try {
        const response = await axios.delete(`${API}/books/${book.id}`);
        parseItem(response, 200);
        return book.id
    } catch (error) {
        console.error(error)
        return null;
    }
}
const addBook = async function (book) {
    try {
        const response = await axios.post(`${API}/books`, book)
        const addedBook = parseItem(response, 201);
        return addedBook;
    }
    catch (error) {
        console.error(error);
        return null;
    }
}
const addUser = async function (user) {
    try {
        const response = await axios.post(`${API}/users`, user)
        const addedUser = parseItem(response, 201);
        return addedUser;
    }
    catch (error) {
        console.error(error);
        return null;
    }
}
const getUsers = async function () {
    try {
        const response = await axios.get(`${API}/users`);
        let user = parseList(response);
        return user;
    } catch (error) {
        console.error(error);
        return [];
    }
};
const deleteUser = async function (user) {
    try {
        const response = await axios.delete(`${API}/users/${user.id}`);
        parseItem(response, 200);
        return user.id
    } catch (error) {
        console.error(error)
        return null;
    }
}
const updateBook = async function (book) {
    try {
        const response = await axios.put(`${API}/books/${book.id}`, book);
        const updatedBook = parseItem(response, 200);
        return updatedBook;
    } catch (error) {
        console.error(error);
        return null;
    }
}
const updateUser = async function (user) {
    try {
        const response = await axios.put(`${API}/users/${user.id}`, user);
        const updatedUser = parseItem(response, 200);
        return updatedUser;
    } catch (error) {
        console.error(error);
        return null;
    }
}
const parseList = response => {
    if (response.status !== 200) throw Error(response.message);
    if (!response.data) return [];
    let list = response.data;
    if (typeof list !== 'object') {
        list = [];
    }
    return list;
};

export const parseItem = (response, code) => {
    if (response.status !== code) throw Error(response.message);
    let item = response.data;
    if (typeof item !== 'object') {
        item = undefined;
    }
    return item;
};

export const dataService = {
    getBooks,
    deleteBook,
    addBook,
    addUser,
    getUsers,
    deleteUser,
    updateBook,
    updateUser
}