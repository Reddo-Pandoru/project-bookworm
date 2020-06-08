<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-sm-12">
        <h2>Aggiungere nuovo libro</h2>
      </div>
    </div>
    <div class="row">
      <div class="col-sm-12">
        <div class="card">
          <div class="card-body">
            <form novalidate data-vv-scope="create-book-form">
              <div class="row">
                <div class="col-lg-6 form-group">
                  <label>Nome</label>
                  <input
                    type="text"
                    name="title"
                    class="form-control"
                    v-model="book.title"
                    v-validate="'required'"
                  />
                  <div
                    v-if="errors.has('create-book-form.title')"
                    class="invalid-feedback"
                  >{{ errors.first('create-book-form.title') }}</div>
                </div>
                <div class="col-lg-6 form-group">
                  <label>ISBN</label>
                  <input
                    type="text"
                    name="ISBN"
                    class="form-control"
                    v-model="book.ISBN"
                    v-validate="'required'"
                  />
                  <div
                    v-if="errors.has('create-book-form.ISBN')"
                    class="invalid-feedback"
                  >{{ errors.first('create-book-form.ISBN') }}</div>
                </div>
                <div class="col-lg-6 form-group">
                  <label>Copie</label>
                  <input
                    type="number"
                    name="copies"
                    class="form-control"
                    v-model="book.copies"
                    v-validate="{required: true, numeric:true}"
                  />
                  <div
                    v-if="errors.has('create-book-form.copies')"
                    class="invalid-feedback"
                  >{{ errors.first('create-book-form.copies') }}</div>
                </div>
                <div class="col-lg-6 form-group">
                  <label>Copie per il prestito</label>
                  <input
                    type="number"
                    name="copies_available"
                    class="form-control"
                    v-model="book.copies_available"
                    v-validate="{required: true, numeric:true, max_value: book.copies}"
                  />
                  <div
                    v-if="errors.has('create-book-form.copies_available')"
                    class="invalid-feedback"
                  >{{ errors.first('create-book-form.copies_available') }}</div>
                </div>
                <div class="col-lg-12 form-group">
                  <label>trama</label>
                  <textarea
                    type="text"
                    name="summary"
                    class="form-control"
                    v-model="book.summary"
                    v-validate="'required'"
                  />
                  <div
                    v-if="errors.has('create-book-form.summary')"
                    class="invalid-feedback"
                  >{{ errors.first('create-book-form.summary') }}</div>
                </div>
              </div>
            </form>
            <div class="row">
              <div class="col-sm-12 d-flex">
                <div class="ml-auto">
                  <button class="btn btn-lg btn-primary mr-2" @click="saveBook()">Save</button>
                  <button class="btn btn-lg btn-secondary" @click="cancel()">Cancel</button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';
import { notifier } from '@/shared/messages/';
export default {
  name: 'CreateBook',
  data() {
    return {
      book: {
        id: '',
        title: '',
        ISBN: '',
        copies: '',
        copies_available: '',
        loan_history: [],
        loan_to: '',
        summary: ''
      }
    };
  },
  methods: {
    ...mapActions(['addBookAction']),
    saveBook() {
      this.$validator.validateAll('create-book-form').then(
        async function(valid) {
          if (valid) {
            // Check if book ISBN exists
            // If doesnt then create book
            if (this.getBookByISBN(this.book.ISBN) === undefined) {
              await this.addBookAction(this.book);
              this.$router.push({ name: 'home' });
              // Else show error
            } else {
              notifier.alert(`Book cant created because this ISBN <b>${this.book.ISBN}</b> exists `);
            }
          }
        }.bind(this)
      );
    },
    cancel() {
      this.$router.push({ name: 'home' });
    }
  },
  computed: {
    ...mapGetters(['getBookByISBN'])
  }
};
</script>

<style>
</style>