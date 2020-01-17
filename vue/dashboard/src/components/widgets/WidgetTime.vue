<template>
    <div class="WidgetTime">
        <div class="container">
            <div class="col-md-12">
                <h3 v-if="error">Loading</h3>
                <div v-else>
                    <h2>{{flag}} {{city}}</h2>
                    <p style="font-size:40px;">{{hour}}</p>
                    <p><strong>{{date}}</strong><br>{{country}}</p>
                </div>

            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "WidgetTime",
    props: ['widget'],
    data () {
        return {
            city: null,
            hour: null,
            date: null,
            country: null,
            flag: null,
            datas: null,
            error: true,
            moment: require('moment-timezone'),

        }
    },
    methods: {
        update_widgets: function() {
            this.$http.get('https://api.opencagedata.com/geocode/v1/json?key=1a27dbe0019e4382914e7c633c4e5f5b&q='+this.city+'&pretty=1')
                .then((response) => {
                    this.datas = response.data;                    
                    var timezone = this.datas.results[0].annotations.timezone.name;
                    var date = this.moment().tz(timezone).format();
                    var date = new Date(date).toUTCString().split(' ');
                    this.hour = date[4];
                    this.date = date[0]+" "+date[1]+" "+date[2]+" "+date[3];
                    this.country = this.datas.results[0].components.country;
                    this.flag = this.datas.results[0].annotations.currency.flag;
                    this.error = false;
                }, (error) => {
                    this.error = true;
                });
        }
    },
    beforeMount(){
        this.widget.datas = JSON.parse(this.widget.datas);
        this.city = this.widget.datas.city;
        this.update_widgets();
        setInterval(this.update_widgets, this.widget.refresh_time*60*1000);
    },
}
</script>
<style scoped>
</style>