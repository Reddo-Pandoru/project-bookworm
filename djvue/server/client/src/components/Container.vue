<template>
  <div class="row">
  <div class="col-lg-6" > 
    <table class="table">
      <thead>
        <th>url</th>
        <th>Title</th>
        <th>Body</th>
        <th>Edit</th>
        <th>Delete</th>
      </thead>
      <tbody>
        <tr v-for="book in books" v-bind:key="book.url">
          <td>{{book.url}}</td>
          <td>{{book.isbn}}</td>
          <td>{{book.book_name}}</td>
          <td>{{book.book_plot}}</td>
          <td>
            <button @click="getOne(book)" class="btn bn-sm btn-success"><i class="fa fa-pencil" aria-hidden="true"></i></button>
          </td>
           <td>
            <button @click="deleteOne(book.url)" class="btn bn-sm btn-success"><i class="fa fa-trash"></i></button>
          </td>
        </tr>
      </tbody>

    </table>
  </div>
 
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Container',
  props: {
    msg: String
  },
  data(){
    return{
      book:null,
      id:'',
      url:'',



    }
  },
  mounted(){
    this.getAll();
  },
  methods:{
    getAll(){
      axios.get('http://localhost:8000/books/9788804637134').then((res)=>{
        console.log(res.data);
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
