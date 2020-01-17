<template>
    <div class="WidgetActorsMatch">
        <div class="container">
            <div class="col-md-12">
                    <h2>Actors Match</h2>
                    <input v-model="actor1" class="form-control in1" type="text" placeholder="Actor 1" @keyup.enter="search()">
                    <input v-model="actor2" class="form-control" type="text" placeholder="Actor 2" @keyup.enter="search()">
                    <br>
                    <div style="height: 100px; overflow-y: auto;" v-if="movies && movies.length > 0">
                        <p>
                            <span v-for="movie in movies">{{movie.title}}<br></span>
                        </p>
                    </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "WidgetActorsMatch",
    props: ['widget'],
    data () {
        return {
            actor1: "Morgan Freeman",
            actor2: "Kevin Spacey",
            movies: null,
            datas: null,
        }
    },
    methods: {
        search: function() {
            this.$http.get('http://localhost:5005/api/movie_compare/'+this.actor1+";"+this.actor2)
                .then((response) => {
                    this.datas = response.data;
                    this.movies = this.datas.results;
                });
        }
    }
}
</script>
<style scoped>
.form-control {
    height: 30px;
}

.in1 {
    margin-bottom: 3px;
}
</style>