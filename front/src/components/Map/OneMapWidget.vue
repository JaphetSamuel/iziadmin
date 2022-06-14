<template>
    <div>
        <a-spin v-if="loading"/>
        <l-map v-else :center="center" :zoom="12" :style="{'height': '80vh'}" >
            <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
            <l-polyline  :color="color" :lat-lngs="polygones">
                <l-popup > <span> Yay I was opened by {{polygone}}</span></l-popup>
            </l-polyline>
            <l-marker :lat-lng="from"/>
            <l-marker :lat-lng="to"/>
        </l-map>
    </div>
</template>

<script>
import { LMap, LMarker,LPolyline, LPopup } from "vue2-leaflet";

export default {
    components: { LMap, LMarker, LPolyline, LPopup },
    props:{
        polygone:"",
        marker:Array,
        color:"blue"
    },
    data:function(){
        console.log(this.$props.polygone);
        return {
            url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
            attribution:'&copy; <a target="_blank" href="http://osm.org/copyright">OpenStreetMap</a> contributors',
            center: [5.326607, -4.022139],
            polygones:[],
            loading:true,
            from:[],
            to:[],
        }
    },
    beforeMount:function(){ 
            var tab = []
            setTimeout(() => {
            tab =  JSON.parse(this.$props.polygone)
            tab = tab.map(function(element) {
                return element.reverse()
            }, this);
            console.log(tab);
            this.from = tab[0]
            this.to = tab[tab.length-1]
            this.polygones  = tab
            this.loading = false
            }, 1000);
            

            
    },
}

</script>