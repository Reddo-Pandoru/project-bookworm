<template>
  <div class="container-fluid">
    <Loading :msg="message" v-if="loading"></Loading>
    <div class="row" v-show="!loading">
      <div class="col-sm-12" v-show="books.length">
        <h2>Libri disponibili {{books.length}}</h2>
      </div>
    </div>
     <input type="text" name="search" class="form control" v-model="search"/>
    <div class="form-row" v-show="!loading">
      <div class="col-lg-6 mb-2 flex-column" v-for="book in books " :key="book.id">
        <div class="card h-100">
          <div class="card-header d-flex">
            <h4
              class="text-truncate flex-grow-1 flex-shrink-1 mb-0 pb-1 align-self-center"
              :title="book.title"
            >{{book.title}}</h4>
            <button
              class="btn btn-lg btn-link flex-grow-0 flex-shrink-0"
              @click="askToDelete(book)"
            >Delete book</button>
          </div>
          <div class="card-body">
            <div class="row">
              <div class="col-sm-12">{{book.summary}}</div>
              <div class="col-lg-6">
                <label>Copie totali</label>
                {{book.copies}}
              </div>
              <div class="col-lg-6">
                <label>Copies disponibili</label>
                {{book.copies_available}}
              </div>
              <div class="col-lg-6">
                <label>{{book.loan_history.filter(h => h.is_loaned === true).length}} Copies loaned</label>
                <ul v-if="book.loan_history.length > 0">
                  <li
                    v-for="(loan, index) in book.loan_history"
                    :key="index"
                    v-show="loan.is_loaned === true"
                  >{{loan.name}}</li>
                </ul>
              </div>
              <div class="col-lg-6">
                <label>ISBN</label>
                {{book.ISBN}}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex';
import Loading from '@/components/loading';
import { notifier } from '@/shared/messages/';
export default {
  name: 'ManageBooks',


  data() {
    
    return {
      message: '',
      loading: false,
      search:''
    };
  },
  components: {
    Loading
  },
  async created() {
    await this.loadBooks();
  },
  methods: {
    ...mapActions(['getBooksAction', 'deleteBookAction']),
    async loadBooks() {
      this.message = 'Getting books please be patient';
      this.loading = true;
      await this.getBooksAction();
      this.message = '';
      this.loading = false;
    },
    askToDelete(book) {
      // Check book If loaned
      // If not loaned then open confirmation message
      if (book.loan_history.filter(h => h.is_loaned === true).length === 0) {
        let onOK = () => this.deleteBook(book);
        let onCancel = () => {
          return;
        };
        notifier.confirm(`Are you sure you want to delete <b>${book.title}</b>`, onOK, onCancel, {
          labels: {
            confirm: 'Delete confirmation'
          }
        });
        // Else show error message
      } else {
        notifier.alert(`Book cant deleted because is loaned by <b>${book.loan_history.map(h => h.name)}</b>`);
      }
    },
    async deleteBook(book) {
      if (book) {
        await this.deleteBookAction(book);
      }
      await this.loadBooks();
    }
  },
  computed: {
    ...mapState(['books']),
    filteredBooks:function(){
      return this.books.filter((books)=>{
        return books.title.match(this.search);
      })
    }
  }
};
</script>
<style scoped lang="scss">
.card {
  min-height: 150px;
}
</style>
