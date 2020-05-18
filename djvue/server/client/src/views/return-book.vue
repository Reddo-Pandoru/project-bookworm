<template>
  <div class="container-fluid">
    <Loading :msg="message" v-if="loading"></Loading>
    <div class="row" v-show="!loading">
      <div class="col-sm-12">
        <h2>Libri in prestito {{returnbooks.length}}</h2>
      </div>
    </div>
    <div class="form-row" v-show="!loading">
      <div
        class="col-lg-6 mb-2 flex-column"
        v-for="(book, index) in books"
        :key="book.id"
        v-show="book.loan_history.length > 0 && isBookLoaned(book)"
      >
        <div class="card h-100">
          <div class="card-header d-flex">
            <h4
              class="text-truncate flex-grow-1 flex-shrink-1 mb-0 pb-1 align-self-center"
              :title="book.title"
            >{{book.title}}</h4>
          </div>
          <div class="card-body">
            <div class="row">
              <div class="col-lg-6 form-group">
                <label></label>
                {{book.loan_history.loan_date}}
              </div>
              <div class="col-lg-6 form-group">
                <label>Restituzione </label>
                <select
                  class="form-control custom-select"
                  :value="book.loan_to"
                  @change="update(`books.${index}.loan_to`, $event)"
                >
                  <option :value="''"></option>
                  <option
                    v-for="user in getUsers(book)"
                    :key="user.id"
                    :value="user.id"
                  >{{user.name}}</option>
                </select>
              </div>
            </div>
            <div class="row" v-show="book.loan_to != ''">
              <div class="col-sm-12">
                <button class="btn btn-block btn-primary" @click="returnBook(book)">Conferma</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapState, mapGetters } from 'vuex';
import { cloneDeep } from 'lodash-es';
import Loading from '@/components/loading';
import fecha from 'fecha';
export default {
  name: 'ReturnBooks',
  components: {
    Loading
  },
  data() {
    return {
      message: '',
      loading: false
    };
  },
  async created() {
    this.message = 'Getting books please be patient';
    this.loading = true;
    await this.loadBooks();
    await this.loadUsers();
    this.message = '';
    this.loading = false;
  },
  methods: {
    ...mapActions(['getBooksAction', 'getUsersAction', 'updateValue', 'updateBookAction', 'updateUserAction']),
    async loadBooks() {
      await this.getBooksAction();
    },
    async loadUsers() {
      await this.getUsersAction();
    },
    getUsers(book) {
      const loan = book.loan_history;
      const users = this.users.filter(p => {
        var canReturn = false;
        // Check each user if have this book and have not returned it yet.
        for (let index = 0; index < loan.length; index++) {
          if (loan[index].id == p.id && loan[index].is_loaned === true) {
            canReturn = true;
          }
        }
        if (canReturn) {
          return p;
        }
      });
      return users;
    },
    async update(path, e) {
      await this.updateValue({ path, value: e.target.value });
    },
    async returnBook(book) {
      const loanbook = cloneDeep(book);
      const loanuser = cloneDeep(this.getUserById(loanbook.loan_to));
      const d = new Date();
      // Set is_loaned to false and return date to current date
      loanbook.loan_history = loanbook.loan_history.map(h => {
        if (h.id === loanuser.id) {
          h.is_loaned = false;
          h.return_date = fecha.format(d, 'DD-MM-YYYY hh:mm');
        }
        return h;
      });
      loanbook.copies_available++;
      loanbook.loan_to = '';
      loanuser.onloan--;
      // Set is_loaned to false and return date to current date
      loanuser.loan_history = loanuser.loan_history.map(h => {
        if (h.id === loanbook.id) {
          h.is_loaned = false;
          h.return_date = fecha.format(d, 'DD-MM-YYYY hh:mm');
        }
        return h;
      });
      await this.updateBookAction(loanbook);
      await this.updateUserAction(loanuser);
    },
    isBookLoaned(book) {
      const isloaned = book.loan_history.filter(h => h.is_loaned === true);
      if (isloaned.length > 0) {
        return true;
      } else {
        return false;
      }
    }
  },
  computed: {
    ...mapGetters(['getUserById']),
    ...mapState(['books', 'users']),
    returnbooks: function() {
      const returnbooks = this.books.filter(p => p.loan_history.length > 0 && this.isBookLoaned(p));
      return returnbooks;
    }
  }
};
</script>
<style scoped lang="scss">
.card {
  min-height: 150px;
}
</style>
