<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-sm-12" >
        <h2>catalogo Libri </h2>
      </div>
    </div>
    <input  type="text" name="name" class="wail" v-model="search"/>
    <span>   </span>
    <button   class="btn btn-primary" type="submit" v-on:click.prevent="getAll()" >Search</button>
    <div class="form-row">
      <div class="col-lg-6 mb-2 flex-column" v-for="book in books " :key="book.isbn">
        <div class="card h-100">
          <div class="card-header d-flex">
            <h4
              class="text-truncate flex-grow-1 flex-shrink-1 mb-0 pb-1 align-self-center"
              :title="book.book_name"
            >{{book.book_name}}</h4>
            <router-link :to="{ name: 'detail', params: { isbn: book.isbn}}" class="nav-item nav-link">Dettagli</router-link>
          </div>
          <div class="card-body">
            <div class="row">
              <div class="col-sm-12">{{book.plot}}</div>
              <div class="col-lg-6">
                <label>ISBN</label>
                {{book.isbn}}
              </div>
              <div class="col-lg-6">
                <label>Lingua</label>
                {{ book.language }} 
              </div>
              <div class="col-lg-6">
                <label>Autori:  </label>
                <span v-for="author in book.author" :key="author.id">{{author}}</span>
              </div>
              <div class="col-lg-6">
                <label>Genere:  </label>
                <span v-for="genere in book.genres" :key="genere.id">{{genere}}</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'ManageBooks',
  data() {
    return {
      books:null,
      copies:Number,
      search:''
    };
  },
  mounted(){
    this.getAll();
  },
  methods: {
    getAll(){
      let url="http://localhost:8000/books";
      if(this.search!==''||this.search!==null) {
            url= `http://localhost:8000/books?search=${this.search}`
          }
      axios.get(url).then((res)=>{
          this.books=res.data;
          console.log(this.books);
      })
    }, 
    filteredBooks:function(){
      return this.books.filter((books)=>{
        return books.book_name.match(this.search)
      })
    }
   /* getCopies(isbn){
      let info;
      let url= 'http://127.0.0.1:8000/volumes/?isbn='+ isbn;
      axios.get(url).then((res)=>{
        console.log(res.data);
        info= res.data.length;
        console.log(info);
      })
    }*/
  },
   /*computed: {
    filteredBooks:function(){
      return this.books.filter((books)=>{
        return books.book_name.match(this.search)
      })
    }
  }*/
}
</script>
<style >
.card {
  min-height: 150px;
}
.wail{
  margin: 0.25rem;
}
</style>