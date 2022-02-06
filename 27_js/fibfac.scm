#lang scheme
;Patrick Ging, Sean Ging Period 1
;K27: Where Does JS Live?
;February 6, 2022

(define (fib num)
  (if (< num 2) num
      (+ (fib (- num 1))
              (fib (- num 2)))))


; (display (fib 10))
; (display "\n")
; (display (fib 7))
; (display "\n")
; (display (fib 3))
; (display "\n")

(define (factorial num)
  (if (= num 0) 1
      (* num (factorial (- num 1)))))
; https://www.mymathtables.com/numbers/100-factorial-tables-chart.html

; (display (factorial 10))
; (display "\n")
; (display (factorial 3))
;(display "\n")
; (display (factorial 1))
; (display "\n")
