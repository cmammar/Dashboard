<template>
    <div class="WidgetTrump">
        <div class="container">
            <div class="col-lg-12">
                <h4>Trump Thoughts</h4>
                <input v-model="query" class="form-control input-lg-8" type="text" placeholder="Hillary" aria-label="Search" @keyup.enter="search()">
                <br>
                <div style="height: 100px; overflow-y: auto;">
                    <p v-for="quote in quotes"><a :href="'https://tronalddump.io/quote/'+quote.quote_id">{{quote.value}}</a></p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "WidgetTrump",
    data () {
        return {
            query: null,
            quotes: null
        }
    },
    methods: {
        search: function() {
            this.$http.get('http://localhost:5005/api/trump/'+this.query)
                .then((response) => {
                    if (response.data.total != 0)
                        this.quotes = response.data._embedded.quotes;
                });
        }
    }
}
</script>
<style scoped>
.form-control {
    height: 30px;
}
</style>