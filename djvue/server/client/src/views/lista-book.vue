<template>
  <section id="books">
    <div class="container">
      <div class="row">
        <div class="col-md-12">
          <h3>{{ title }}</h3>
        </div>
      </div>

      <div v-if="books" class="row">
        <div v-for="book in books" :key="book.id" class="col-md-12 col-lg-4">
          <div class="card">
            <div class="card-block">
              <h3 class="card-title">{{ book.book_name }}</h3>
              <p class="card-text"> <router-link :to="{ name: 'detail', params: { isbn: book.isbn}}">Ver detalles</router-link> </p>
              <!-- <p class="card-text"><i class="fa fa-tag" aria-hidden="true"></i></p> -->
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import axios from 'axios'
export default {
  data () {
    return {
      title: 'Lista di libri',
      message: '',
      books: null
    }
  },
  mounted () {
    // do something after mounting vue instance
    this.getBooks()
  },
  methods: {
    getBooks () {
      let vm = this
      let url = 'http://localhost:8000/books'
      axios.get(url)
        .then(function (response) {
          // Getting Data from response
          if (response.status === 200) {
            console.log(response.data);
            vm.books = response.data
          }
        })
        .catch(function (error) {
          alert(error)
        })
    }
  }
}
</script>

<style scoped lang="scss"></style>