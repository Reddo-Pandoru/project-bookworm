import Vue from 'vue';
import Vuex from 'vuex';
import { set } from 'lodash-es';
import { dataService } from '../shared/data.services';
import {
    ADD_BOOK,
    GET_BOOKS,
    DELETE_BOOK,
    ADD_USER,
    GET_USERS,
    DELETE_USER,
    UPDATE_BOOK,
    UPDATE_VALUE,
    UPDATE_USER
} from './mutation-types'

Vue.use(Vuex);

const state = () => ({
    books: [],
    users: []
});

const mutations = {
    [GET_BOOKS](state, books) {
        state.books = books
    },
    [DELETE_BOOK](state, id) {
        state.books = [...state.books.filter(b =>
            b.id != id
        )];
    },
    [ADD_BOOK](state, book) {
        state.books.push(book)
    },
    [ADD_USER](state, user) {
        state.users.push(user)
    },
    [GET_USERS](state, users) {
        state.users = users
    },
    [DELETE_USER](state, id) {
        state.users = [...state.users.filter(b =>
            b.id != id
        )];
    },
    [UPDATE_VALUE](state, data) {
        set(state, data.path, data.value);
    },
    [UPDATE_BOOK](state, book) {
        const index = state.books.findIndex(h => h.id === book.id);
        state.books.splice(index, 1, book);
        state.books = [...state.books];
    },
    [UPDATE_USER](state, user) {
        const index = state.users.findIndex(h => h.id === user.id);
        state.users.splice(index, 1, user);
        state.users = [...state.users];
    }
};

const actions = {
    async getBooksAction({ commit }) {
        const books = await dataService.getBooks();
        // eslint-disable-next-line no-undef
        commit(GET_BOOKS, books);
    },
    async deleteBookAction({ commit }, book) {
        const deletedBookId = await dataService.deleteBook(book)
        commit(DELETE_BOOK, deletedBookId);
    },
    async addBookAction({ commit }, book) {
        const addedBook = await dataService.addBook(book);
        commit(ADD_BOOK, addedBook);
    },
    async addUserAction({ commit }, user) {
        const addedUser = await dataService.addUser(user);
        commit(ADD_USER, addedUser);
    },
    async getUsersAction({ commit }) {
        const users = await dataService.getUsers();
        // eslint-disable-next-line no-undef
        commit(GET_USERS, users);
    },
    async deleteUserAction({ commit }, user) {
        const deletedUserId = await dataService.deleteUser(user)
        commit(DELETE_USER, deletedUserId);
    },
    async updateBookAction({ commit }, book) {
        const updatedBook = await dataService.updateBook(book);
        // const loanedUser = await dataService.loanUser(loan.user)
        commit(UPDATE_BOOK, updatedBook);
    },
    async updateUserAction({ commit }, user) {
        const updatedUser = await dataService.updateUser(user);
        commit(UPDATE_USER, updatedUser);
    },
    updateValue({ commit }, data) {
        commit(UPDATE_VALUE, data);
    }
};

const getters = {
    getUserById: state => id => state.users.find(h => h.id === id),
    getUserByEmail: state => email => state.users.find(h => h.email === email),
    getBookByISBN: state => ISBN => state.books.find(h => h.ISBN === ISBN)
};

export default new Vuex.Store({
    strict: process.env.NODE_ENV !== 'production',
    state,
    mutations,
    actions,
    getters
});