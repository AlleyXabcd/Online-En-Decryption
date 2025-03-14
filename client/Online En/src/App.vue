<script setup>
import { ref } from 'vue'
import axios from 'axios'

const ways = ref([
  { ischoose: 1, name: "Caesar cipher",keystandard:"数字" },
  { ischoose: 0, name: "Vigenere Cipher",keystandard:"英文字符串" },
  { ischoose: 0, name: "RC4",keystandard:"数字" },
])

const encry = ref("")
const decry = ref("")
const key = ref("")

function selectway(clickedIndex) {
  ways.value = ways.value.map((item, index) => ({
    ...item,
    ischoose: index === clickedIndex ? 1 : 0
  }))
}

function getSelectedAlgorithm() {
  const selected = ways.value.find(item => item.ischoose === 1)
  return selected ? selected.name : null
}

function validateKey(algorithm, key) {
  if (algorithm === "Caesar cipher") {
    return /^\d+$/.test(key)
  } else if (algorithm === "Vigenere Cipher") {
    return /^[a-zA-Z]+$/.test(key)
  } else if (algorithm === "RC4") {
    return /^\d+$/.test(key)
  }
  return false
}

async function encrypt() {
  const algorithm = getSelectedAlgorithm()
  if (!validateKey(algorithm, key.value)) {
    alert(`Invalid key format for ${algorithm}`)
    return
  }

  const response = await axios.post(
    "http://127.0.0.1:8000/api/encrypt", 
    {
      text: encry.value,
      algorithm: algorithm,
      key: key.value
    }
  )
      decry.value = response.data.result

}

async function decrypt() {
  const response = await axios.post(
    'http://127.0.0.1:8000/api/decrypt', 
    {
      text: decry.value,
      algorithm: getSelectedAlgorithm(),
      key: key.value
    }
  )
  encry.value = response.data.result
}
</script>

<template>
  <div class="header">
    <h1>Online En/Decryption</h1>
    <div class="accent-line"></div>
  </div>

  <div class="container">
    <div class="algorithm-selector">
      <div 
        v-for="(item, index) in ways" 
        class="algorithm-card" 
        :class="{ 'selected': item.ischoose }" 
        @click="selectway(index)"
      >
        <div class="card-content">
          <div class="card-icon">🔒</div>
          <div class="card-name">{{ item.name }}</div>
        </div>
      </div>
    </div>

    <div class="crypto-container">
      <div class="input-section">
        <textarea 
          class="crypto-input" 
          placeholder="Enter plain text..."
          v-model="encry"
        ></textarea>
      </div>

      <div class="control-panel">
        <div class="key-input">
          <input 
            type="text" 
            placeholder="Encryption Key"
            v-model="key"
          >
          <div class="tooltip">?
            <div class="tooltip-text">
              密钥规范: {{ ways.find(item => item.ischoose === 1).keystandard }}
            </div>
          </div>
        </div>
        <div class="action-buttons">
          <button class="encrypt-btn" @click="encrypt">
            <span>Encrypt</span>
          </button>
          <button class="decrypt-btn" @click="decrypt">
            <span>Decrypt</span>
          </button>
        </div>
      </div>

      <div class="input-section">
        <textarea 
          class="crypto-input" 
          placeholder="Enter cipher text..."
          v-model="decry"
        ></textarea>
      </div>
    </div>
  </div>
</template>

<style scoped>
.header {
  text-align: center;
  margin-bottom: 20px;
}

.accent-line {
  width: 100%;
  height: 2px;
  background-color: #007BFF;
  margin: 10px 0;
}

.container {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.algorithm-selector {
  display: flex;
  justify-content: center;
  margin-bottom: 20px;
}

.algorithm-card {
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 10px;
  margin: 0 10px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.algorithm-card.selected {
  background-color: #007BFF;
  color: white;
}

.card-content {
  display: flex;
  align-items: center;
}

.card-icon {
  font-size: 24px;
  margin-right: 10px;
}

.crypto-container {
  width: 80%;
  max-width: 600px;
}

.input-section {
  margin-bottom: 20px;
}

.crypto-input {
  width: 100%;
  height: 100px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  resize: none;
}

.control-panel {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.key-input {
  display: flex;
  align-items: center;
}

.key-input input {
  padding: 5px;
  border: 1px solid #ccc;
  border-radius: 5px;
  margin-right: 10px;
}

.tooltip {
  background-color: #007BFF;
  color: white;
  padding: 5px;
  border-radius: 50%;
  cursor: pointer;
  position: relative;
}

.tooltip:hover .tooltip-text {
  visibility: visible;
  opacity: 1;
}

.tooltip-text {
  visibility: hidden;
  width: 200px;
  background-color: #555;
  color: #fff;
  text-align: center;
  border-radius: 6px;
  padding: 5px 0;
  position: absolute;
  z-index: 1;
  bottom: 125%; /* Position the tooltip above the text */
  left: 50%;
  margin-left: -100px;
  opacity: 0;
  transition: opacity 0.3s;
}

.tooltip-text::after {
  content: "";
  position: absolute;
  top: 100%; /* At the bottom of the tooltip */
  left: 50%;
  margin-left: -5px;
  border-width: 5px;
  border-style: solid;
  border-color: #555 transparent transparent transparent;
}

.action-buttons {
  display: flex;
}

.encrypt-btn, .decrypt-btn {
  background-color: #007BFF;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
  margin: 0 5px;
  transition: background-color 0.3s;
}

.encrypt-btn:hover, .decrypt-btn:hover {
  background-color: #0056b3;
}
</style>
