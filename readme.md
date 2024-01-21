Висновки порівняння алгоритмів пошуку:

Стаття #1
                                                                                    
                                                                                    
Алгоритм                       | Підрядок                       | Час виконання, сек
------------------------------------------------------------------------------------
boyer_moore_search             | корисний для                   | 0.003161114000249654
kmp_search                     | корисний для                   | 0.009022315993206576
rabin_karp_search              | корисний для                   | 0.02117072900000494
boyer_moore_search             | розваги вихідного дня          | 0.003348077996633947
kmp_search                     | розваги вихідного дня          | 0.015020696009742096
rabin_karp_search              | розваги вихідного дня          | 0.03527831900282763
                                                                                    
Стаття #2
                                                                                    
                                                                                    
Алгоритм                       | Підрядок                       | Час виконання, сек
------------------------------------------------------------------------------------
boyer_moore_search             | ациклічного графу              | 0.002698925993172452
kmp_search                     | ациклічного графу              | 0.011154520005220547
rabin_karp_search              | ациклічного графу              | 0.026390022001578473
boyer_moore_search             | розваги вихідного дня          | 0.005859704993781634
kmp_search                     | розваги вихідного дня          | 0.022071735002100468
rabin_karp_search              | розваги вихідного дня          | 0.056328523001866415

На основі пошуку по підрядках - існуючому кожній статті відповідно і не існуючому використовуючі три алгоритми пошуку - Боєра-Мура, Кнута-Морріса-Пратта та Рабіна-Карпа, можна зробити висновок, що найшвидшим є алгоритм пошуку Боєра-Мура для обох статтей. Про це свідчить час виконання наведений у таблицях.