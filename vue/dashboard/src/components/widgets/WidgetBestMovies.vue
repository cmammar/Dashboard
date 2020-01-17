<template>
    <div class="WidgetBestMovies">
        <div class="container">
            <div class="col-md-12">
                <h3 v-if="error">Loading</h3>
                <div v-else>
                    <h2>Movie Ranking {{country_code}}</h2>
                    <div style="height: 150px; overflow-y: auto;">
                    <p>
                        <span v-for="movie in movies">{{movie.title}}<br></span>
                    </p>
                    </div>
                </div>

            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "WidgetBestMovies",
    props: ['widget'],
    data () {
        return {
            country_code: null,
            movies: null,
            datas: null,
            error: true,
        }
    },
    methods: {
        update_widgets: function() {
            this.$http.get('https://api.themoviedb.org/3/movie/top_rated?api_key=0d5a9f64db3ef47c0a9e1e447debb789&language=fr&page=1&region='+this.country_code)
                .then((response) => {
                    this.datas = response.data;
                    this.movies = this.datas.results;
                    this.error = false;
                }, (error) => {
                    this.error = true;
                });
        }
    },
    beforeMount(){
        this.widget.datas = JSON.parse(this.widget.datas)
        this.country_code = this.widget.datas.country_code;
        this.update_widgets();
        setInterval(this.update_widgets, this.widget.refresh_time*60*1000);
    },
}
</script>
<style scoped>
</style>