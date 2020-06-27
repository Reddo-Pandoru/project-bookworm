<template>
    <div class="container pt-5 " v-if="book">
            <h3>{{ book.book_name }}</h3>
            
            <hr>
            <div class="row" >
                <div class="col-3 border-right">
                  <img v-bind:src="book.book_image" class="img-fluid"  width="200" height="200"  alt="image">
                  <p><b>ISBN:</b>{{book.isbn}}</p>
                </div>
                <div class="col-5 ">
                  <h5>{{book.book_plot}} </h5>
                   

                </div>


                <div class="col-4 border-left">
                    <p><b>Autori:</b> <span  v-for="author in book.author" :key="author.id"> {{author}} </span> 
                    <p><b>Generi:</b> <span  v-for="genere in book.genres" :key="genere.id"> {{genere}} </span>
                    <p><b>Editore:</b> {{book.editor}}</p>
                    <p><b>Sezione:</b>{{book.sezione}}</p>
                    <p><b>Numero di pagine:</b> {{book.book_pages_number ? book.book_pages_number : '-'}}</p>
                     <p><b>Data di pubblicazione:</b> {{book.book_release_date}}</p>
                </div>
        </div>
      </div>
</template>
<script>
import axios from 'axios'
export default {
  name: 'book-details',
  
  mounted () {
    // do something after mounting vue instance
    this.getBookDetails()
  },
  data: () => ({
    message: '',
    book: null
  }),
  methods: {
    getBookDetails () {
      let vm = this
      let url = 'http://localhost:8000/books/' + this.$route.params.isbn;
      console.log(url)
      axios.get(url)
        .then(function (response) {
          // Getting Data from response
          if (response.status === 200) {
            vm.book = response.data
            console.log(vm.book)
          }
        })
        .catch(function (error) {
          alert(error)
        })
    }
  }
}
</script>
<style lang="scss" scoped>


</style>