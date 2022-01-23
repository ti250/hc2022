<!-- Essentially https://dev.to/nelsoncode/how-to-use-the-webcam-with-svelte-js-2415 -->
<script>
    import { push } from 'svelte-spa-router';
    import { scale } from 'svelte/transition';
    import { feedback, pastShops } from './store';

    let videoSource = null;
    let loading = false;
    let processing = false;
    const scratchCanvas = document.createElement('canvas');

    const getCamera = async () => {
        try {
            loading = true;
            const stream = await navigator.mediaDevices.getUserMedia({
                // video: true,
                video: { facingMode: "environment" }
            });
            videoSource.srcObject = stream;
            videoSource.play();
            loading = false;
        } catch (error) {
            console.log(error);
        }
    };

    getCamera();

    function takePhoto() {
        console.log("Take Photo Called");
        processing = true;
        scratchCanvas.width = videoSource.videoWidth;
        scratchCanvas.height = videoSource.videoHeight;
        const scratchContext = scratchCanvas.getContext('2d');
        scratchContext.drawImage(videoSource, 0, 0, videoSource.videoWidth, videoSource.videoHeight);
        scratchCanvas.toBlob(
            function (jpegBlob) {
                const formData = new FormData();
                formData.append("photo", jpegBlob);

                fetch("/api/analyse_receipt",
                {
                    method: "POST",
                    body: formData
                })
                .then(response => {
                    return response.json();
                })
                .then(jsonified => {
                    feedback.set(jsonified);
                    console.log(jsonified);
                    let newOldShop = {
                        locationName: jsonified.locationName,
                        cost: jsonified.actualTotal,
                        locationType: jsonified.locationType,
                        date: "23/Jan"
                    }
                    let localPastShops = $pastShops;
                    localPastShops.reverse();
                    localPastShops.push(newOldShop);
                    localPastShops.reverse();
                    pastShops.set(localPastShops);
                })
                .then(() => {
                    push("/receiptFeedback");
                })
            }, 'image/jpeg'
        )
    }
</script>

<div id="content" in:scale>
    <video id="cameraView" bind:this={videoSource} playsinline />
    <div>
        <button onclick="window.history.back()" id="backbutton">
            &lt; Back
        </button>
    </div>
    {#if loading}
        <h1>Loading Camera...</h1>
    {/if}
    <div class="photo-button">
        <button on:click={takePhoto} class="photo-button">
        </button>
    </div>
    {#if processing}
    <div id="processingOverlay">
        <div id="processingContent">
            <h1>
                Processing...
            </h1>
            <h2>
                Our helper robots are working real hard on this one, hang on tight!
            </h2>
        </div>
    </div>
    {/if}
</div>

<style>
    
    h1 {
        font-weight: 700;
        position: absolute;
        margin-left: 55px;
        margin-top: 200px;
    }

    h2 {
        text-align: center;
    }

    #backbutton {
        position:  absolute;
        border-color: white;
        padding: 20px;
        margin: 20px;
        color: SandyBrown;
        border-radius: 40px;
        padding: 20px;
        z-index: 100;
    }

    #content {
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-color: black;
        color: white;
    }

    #cameraView {
        width: 95%;
        position: absolute;
        top: 50%;
        left: 50%;
        margin-right: -50%;
        transform: translate(-50%, -50%);
        border-radius: 20px;
    }

    #processingOverlay {
        background-color: rgba(0, 0, 0, 0.7);
        width: 100%;
        height: 100%;
        position: absolute;
        top: 50%;
        left: 50%;
        margin-right: -50%;
        transform: translate(-50%, -50%);
        z-index: 10000000;
    }

    #processingContent {
        background-color: rgba(0, 0, 0, 0.0);
        position: absolute;
        top: 50%;
        left: 50%;
        margin-right: -50%;
        transform: translate(-50%, -50%);
        z-index: 10000001;
    }

    .photo-button {
      width: 100px;
      height: 100px;
      top: 85%;
      left: 50%;
      margin-top: -50px;
      margin-left: -50px;
      position: absolute;
      border-radius: 100%;
    }

</style>
