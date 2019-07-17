<template>
  <div id="app" v-if="current">
    <youtube
      :video-id="current.videoid"
      :player-vars="playerVars"
      ref="youtube"
      @playing="playing"
      @ended="ended"
    ></youtube>
    <!-- <button @click="playVideo">play</button> -->
  </div>
</template>

<script>
import HelloWorld from "./components/HelloWorld.vue";
import { api } from "@/utils/api.js";

export default {
  name: "app",
  data() {
    return {
      current: "",
      videos: [],
      playerVars: {
        autoplay: 1
      }
    };
  },
  methods: {
    playVideo() {
      this.player.playVideo();
    },
    playing() {
      console.log("o/ we are watching!!!");
    },
    ended() {
      console.log("Video had ended!");
      this.current = this.videos.shift();
      // this.videoId = "yf5qrVdD9E0";
      console.log("Starting new videos!");
      this.player.playVideo();
    }
  },
  computed: {
    player() {
      return this.$refs.youtube.player;
    }
  },
  created() {
    let self = this;
    api("query{videos{videoid}}").then(data => {
      console.log(data.videos);
      self.current = data.videos.shift();
      self.videos = data.videos;
    });
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
