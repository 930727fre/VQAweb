<template>
  <main data-layername="tapQuest" class="flex flex-col">
    <section data-layername="layout" class="flex overflow-hidden flex-col w-full bg-white max-md:max-w-full">
      <div data-layername="bb" class="flex flex-col px-10 pt-6 pb-11 w-full bg-pink-100 max-md:px-5 max-md:max-w-full">
        <div data-layername="background" class="flex flex-col items-end pb-11 rounded-xl bg-gray-300 bg-opacity-50 shadow-[8px_8px_20px_rgba(0,0,0,0.25)] max-md:max-w-full">
          <header data-layername="top" class="flex flex-col items-center self-stretch px-20 rounded-xl bg-slate-500 bg-opacity-80 max-md:px-5 max-md:max-w-full">
            <img loading="lazy" src="https://cdn.builder.io/api/v1/image/assets/TEMP/b7a590f92b1f65a24ce07a05473b37fdc1b29cc5729fff5e9a9b073888d5dac0?placeholderIfAbsent=true&apiKey=c9bff0a3a0134cf2b1616c259a379779" alt="TapQuest Logo" class="object-contain z-10 -mt-6 mb-0 w-60 max-w-full aspect-[1.21] max-md:mb-2.5" />
          </header>
          <div data-layername="qOutput" class="flex shrink-0 mt-14 mr-28 max-w-full bg-rose-400 rounded-xl h-[196px] w-[567px] max-md:mt-10 max-md:mr-2.5" role="region" aria-label="Question Output"></div>
          <div class="flex flex-col mt-4 mr-11 w-full text-2xl text-white max-w-[1661px] max-md:mr-2.5 max-md:max-w-full">
            <div data-layername="aOutput" class="flex shrink-0 max-w-full bg-rose-200 rounded-xl h-[196px] w-[567px]" role="region" aria-label="Answer Output"></div>
            <div class="flex flex-wrap gap-7 mt-64 max-md:mt-10">
              <div class="flex flex-wrap flex-auto max-md:max-w-full">
                <button data-layername="picInput" class="px-8 py-7 rounded-xl bg-slate-500 max-md:px-5 max-md:max-w-full" aria-label="Upload the picture">
                  Upload the picture
                </button>
                <div data-layername="mid" class="flex shrink-0 bg-sky-900 h-[81px] w-[51px]" role="separator"></div>
                <form data-layername="charInput" class="px-7 py-8 bg-blue-400 rounded-none max-md:px-5 max-md:max-w-full">
                  <label for="questionInput" class="sr-only">Type your Question</label>
                  <input type="text" id="questionInput" placeholder="Type your Question" aria-label="Type your Question" class="w-full bg-transparent text-white placeholder-white::placeholder focus:outline-none" />
                </form>
              </div>
              <button aria-label="Submit Question" class="my-auto">
                <img loading="lazy" src="https://cdn.builder.io/api/v1/image/assets/TEMP/ef0da4e27e3e6a7f0881fa26df0b9dc0dd2e50030ed6424867504ead3b4e6e67?placeholderIfAbsent=true&apiKey=c9bff0a3a0134cf2b1616c259a379779" alt="" class="object-contain shrink-0 aspect-square shadow-[0px_4px_4px_rgba(0,0,0,0.25)] w-[74px]" />
              </button>
            </div>
          </div>
        </div>
      </div>
    </section>
  </main>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'TapQuest',
  // Component logic goes here
});
</script>